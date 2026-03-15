#!/usr/bin/env python3
"""Generate consolidated Meridian readiness dashboard from multiple instances.

Reads session-activity-log.md from each Meridian instance, merges daily
aggregates, and produces a unified HTML dashboard showing cross-instance
health metrics.

Usage:
    python3 generate-consolidated.py

Output:
    consolidated.html (local)

Instances are configured in INSTANCES below. Each entry specifies the
log path and the number of domain area columns (personal has 5, consulting
has 3). The generator parses each log independently, then merges by date.
"""

import re
from datetime import datetime
from pathlib import Path

OUTPUT_FILE = Path(__file__).resolve().parent / "consolidated.html"

# Instance configurations — area columns differ per instance
INSTANCES = [
    {
        "name": "Personal",
        "log": Path.home() / "Projects" / "personal" / "current-state" / "session-activity-log.md",
        "areas": ["condo_board", "home_lab", "birw", "tavr", "church"],
        "area_labels": {
            "condo_board": "Condo Board", "home_lab": "Home Lab",
            "birw": "BIRW", "tavr": "TAVR", "church": "Church",
        },
        "color": "#6c8cff",
        "domain_color": "#4ade80",
        "dashboard_url": "personal.html",
    },
    {
        "name": "Consulting",
        "log": Path.home() / "Projects" / "consulting" / "current-state" / "session-activity-log.md",
        "areas": ["maam", "content", "practice"],
        "area_labels": {
            "maam": "MaAM", "content": "Content", "practice": "Practice",
        },
        "color": "#f59e0b",
        "domain_color": "#06b6d4",
        "dashboard_url": "consulting.html",
    },
]


def parse_duration_minutes(raw: str) -> float:
    """Parse a human-written duration into minutes."""
    raw = raw.strip().lower()
    if not raw or raw in ("—", ""):
        return 25.0
    if raw == "short":
        return 10.0
    raw = re.sub(r"[~()]", "", raw)
    raw = re.sub(r"intermittent", "", raw).strip()
    h_match = re.search(r"(\d+(?:\.\d+)?)\s*h", raw)
    if h_match:
        return float(h_match.group(1)) * 60
    m_match = re.search(r"(\d+)\s*min", raw)
    if m_match:
        return float(m_match.group(1))
    return 10.0


def parse_count(val: str) -> int:
    val = val.replace("—", "0").replace("all", "0").strip()
    match = re.search(r"(\d+)", val)
    return int(match.group(1)) if match else 0


def parse_instance(inst: dict) -> dict:
    """Parse a single instance's activity log and return aggregated data."""
    content = inst["log"].read_text()
    areas = inst["areas"]
    # Expected columns: Session, Time, Duration, [areas...], meridian, Outputs, Notes
    min_cols = 3 + len(areas) + 1 + 1  # session+time+dur + areas + meridian + outputs

    sessions = []
    current_day = None
    current_date = None

    for line in content.split("\n"):
        day_match = re.match(r"### Day (\d+) — (\d{4}-\d{2}-\d{2})", line)
        if day_match:
            current_day = int(day_match.group(1))
            current_date = day_match.group(2)
            continue

        if current_date and line.startswith("|") and not line.startswith("|---") and not line.startswith("| Session"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= min_cols:
                duration_min = parse_duration_minutes(cells[2])
                area_counts = {}
                for i, a in enumerate(areas):
                    area_counts[a] = parse_count(cells[3 + i])
                meridian_idx = 3 + len(areas)
                meridian = parse_count(cells[meridian_idx])

                total_changes = sum(area_counts.values()) + meridian
                domain_min = 0
                meridian_min = 0
                if total_changes > 0:
                    domain_min = duration_min * sum(area_counts.values()) / total_changes
                    meridian_min = duration_min * meridian / total_changes
                else:
                    meridian_min = duration_min

                # Extract observation count from outputs
                outputs_idx = meridian_idx + 1
                outputs = cells[outputs_idx] if len(cells) > outputs_idx else ""
                mo_count = len(re.findall(r"MO-\d+", outputs))

                sessions.append({
                    "day": current_day,
                    "date": current_date,
                    "duration_min": duration_min,
                    "domain_min": domain_min,
                    "meridian_min": meridian_min,
                    "mo_count": mo_count,
                })

    # Aggregate by date
    by_date = {}
    for s in sessions:
        d = s["date"]
        if d not in by_date:
            by_date[d] = {
                "date": d, "sessions": 0, "duration_min": 0,
                "domain_min": 0, "meridian_min": 0, "mo_count": 0,
            }
        by_date[d]["sessions"] += 1
        by_date[d]["duration_min"] += s["duration_min"]
        by_date[d]["domain_min"] += s["domain_min"]
        by_date[d]["meridian_min"] += s["meridian_min"]
        by_date[d]["mo_count"] += s["mo_count"]

    daily = sorted(by_date.values(), key=lambda x: x["date"])

    total_sessions = sum(d["sessions"] for d in daily)
    total_min = sum(d["duration_min"] for d in daily)
    total_domain_min = sum(d["domain_min"] for d in daily)
    total_infra_min = sum(d["meridian_min"] for d in daily)
    domain_pct = round(total_domain_min / total_min * 100) if total_min else 0
    total_obs = sum(d["mo_count"] for d in daily)

    return {
        "name": inst["name"],
        "color": inst["color"],
        "domain_color": inst["domain_color"],
        "dashboard_url": inst["dashboard_url"],
        "areas": inst["areas"],
        "area_labels": inst["area_labels"],
        "daily": daily,
        "total_sessions": total_sessions,
        "total_min": total_min,
        "total_domain_min": total_domain_min,
        "total_infra_min": total_infra_min,
        "domain_pct": domain_pct,
        "total_obs": total_obs,
        "days": len(daily),
    }


def merge_daily(instances: list) -> list:
    """Merge daily data across instances by date."""
    all_dates = set()
    for inst in instances:
        for d in inst["daily"]:
            all_dates.add(d["date"])

    merged = []
    for date in sorted(all_dates):
        entry = {
            "date": date, "sessions": 0, "duration_min": 0,
            "domain_min": 0, "meridian_min": 0, "mo_count": 0,
        }
        for inst in instances:
            for d in inst["daily"]:
                if d["date"] == date:
                    entry["sessions"] += d["sessions"]
                    entry["duration_min"] += d["duration_min"]
                    entry["domain_min"] += d["domain_min"]
                    entry["meridian_min"] += d["meridian_min"]
                    entry["mo_count"] += d["mo_count"]
        merged.append(entry)
    return merged


def fmt_hours(minutes: float) -> str:
    h = int(minutes // 60)
    m = int(minutes % 60)
    return f"{h}h {m}m" if h > 0 else f"{m}m"


def generate_html(instances: list, merged: list) -> str:
    """Generate consolidated dashboard HTML."""
    total_sessions = sum(d["sessions"] for d in merged)
    total_min = sum(d["duration_min"] for d in merged)
    total_domain_min = sum(d["domain_min"] for d in merged)
    total_infra_min = sum(d["meridian_min"] for d in merged)
    domain_pct = round(total_domain_min / total_min * 100) if total_min else 0
    total_obs = sum(d["mo_count"] for d in merged)
    total_days = len(merged)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # JS data for merged timeline
    date_labels = [d["date"] for d in merged]
    merged_domain_hrs = [round(d["domain_min"] / 60, 2) for d in merged]
    merged_infra_hrs = [round(d["meridian_min"] / 60, 2) for d in merged]
    merged_total_hrs = [round(d["duration_min"] / 60, 2) for d in merged]
    merged_sessions = [d["sessions"] for d in merged]
    merged_obs = [d["mo_count"] for d in merged]
    merged_domain_pcts = [
        round(d["domain_min"] / d["duration_min"] * 100) if d["duration_min"] else 0
        for d in merged
    ]

    # Per-instance daily domain % for comparison chart
    inst_domain_pct_series = []
    for inst in instances:
        inst_by_date = {d["date"]: d for d in inst["daily"]}
        series = []
        for date in date_labels:
            d = inst_by_date.get(date)
            if d and d["duration_min"] > 0:
                series.append(round(d["domain_min"] / d["duration_min"] * 100))
            else:
                series.append(None)
        inst_domain_pct_series.append(series)

    # Per-instance daily hours for stacked comparison
    inst_hours_series = []
    for inst in instances:
        inst_by_date = {d["date"]: d for d in inst["daily"]}
        series = [round(inst_by_date.get(date, {"duration_min": 0})["duration_min"] / 60, 2) for date in date_labels]
        inst_hours_series.append(series)

    # Donut data: domain vs infra per instance
    donut_labels = []
    donut_data = []
    donut_colors = []
    for inst in instances:
        donut_labels.append(f"{inst['name']} Domain")
        donut_data.append(round(inst["total_domain_min"] / 60, 1))
        donut_colors.append(inst["domain_color"] + "cc")
    for inst in instances:
        donut_labels.append(f"{inst['name']} Infra")
        donut_data.append(round(inst["total_infra_min"] / 60, 1))
        donut_colors.append("#818cf8cc")

    # Status determination
    if domain_pct >= 80:
        status = "Operational"
        status_bg = "rgba(74,222,128,0.15)"
        status_color = "var(--domain)"
        gauge_color = "#4ade80"
        pct_color = "var(--domain)"
    elif domain_pct >= 60:
        status = "Transitioning"
        status_bg = "rgba(245,158,11,0.15)"
        status_color = "#f59e0b"
        gauge_color = "#f59e0b"
        pct_color = "#f59e0b"
    else:
        status = "Prototype"
        status_bg = "rgba(129,140,248,0.15)"
        status_color = "var(--infra)"
        gauge_color = "#818cf8"
        pct_color = "var(--infra)"

    # Instance cards HTML
    inst_cards_html = ""
    for inst in instances:
        i_status = "Operational" if inst["domain_pct"] >= 80 else "Transitioning" if inst["domain_pct"] >= 60 else "Prototype"
        i_bg = "rgba(74,222,128,0.15)" if inst["domain_pct"] >= 80 else "rgba(245,158,11,0.15)" if inst["domain_pct"] >= 60 else "rgba(129,140,248,0.15)"
        i_color = "var(--domain)" if inst["domain_pct"] >= 80 else "#f59e0b" if inst["domain_pct"] >= 60 else "var(--infra)"
        areas_str = ", ".join(inst["area_labels"].values())
        inst_cards_html += f"""
      <a href="{inst['dashboard_url']}" class="inst-card" style="border-left: 3px solid {inst['color']}">
        <div class="inst-header">
          <h3>{inst['name']}</h3>
          <span class="inst-status" style="background: {i_bg}; color: {i_color};">{i_status}</span>
        </div>
        <div class="inst-metrics">
          <div class="inst-metric">
            <div class="inst-metric-val" style="color: {inst['color']}">{inst['domain_pct']}%</div>
            <div class="inst-metric-label">Domain</div>
          </div>
          <div class="inst-metric">
            <div class="inst-metric-val">{fmt_hours(inst['total_min'])}</div>
            <div class="inst-metric-label">Total</div>
          </div>
          <div class="inst-metric">
            <div class="inst-metric-val">{inst['total_sessions']}</div>
            <div class="inst-metric-label">Sessions</div>
          </div>
          <div class="inst-metric">
            <div class="inst-metric-val">{inst['days']}</div>
            <div class="inst-metric-label">Days</div>
          </div>
          <div class="inst-metric">
            <div class="inst-metric-val">{inst['total_obs']}</div>
            <div class="inst-metric-label">Observations</div>
          </div>
        </div>
        <div class="inst-areas">Areas: {areas_str}</div>
        <span class="inst-arrow">&#8599; View dashboard</span>
      </a>
"""

    # Null-safe JSON for per-instance series (replace None with "null")
    def to_js_array(arr):
        return "[" + ",".join("null" if v is None else str(v) for v in arr) + "]"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Meridian — Consolidated Readiness</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
  :root {{
    --bg: #0f1117; --surface: #1a1d27; --border: #2a2d3a;
    --text: #e0e0e8; --text-dim: #8888a0; --accent: #6c8cff;
    --domain: #4ade80; --infra: #818cf8;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif;
    background: var(--bg); color: var(--text); padding: 24px; line-height: 1.5;
  }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}

  .header {{
    display: flex; justify-content: space-between; align-items: baseline;
    margin-bottom: 24px; border-bottom: 1px solid var(--border); padding-bottom: 16px;
  }}
  .header h1 {{ font-size: 22px; font-weight: 600; letter-spacing: -0.3px; }}
  .header .subtitle {{
    font-size: 13px; color: var(--text-dim); margin-top: 4px;
    display: flex; align-items: center; gap: 12px;
  }}
  .header .subtitle .status-badge {{
    font-size: 10px; text-transform: uppercase; letter-spacing: 0.6px;
    font-weight: 600; padding: 2px 8px; border-radius: 3px;
  }}
  .header .updated {{ font-size: 13px; color: var(--text-dim); }}
  .header .nav {{ font-size: 13px; color: var(--text-dim); }}

  /* Readiness banner */
  .readiness {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
    padding: 24px; margin-bottom: 24px;
    display: grid; grid-template-columns: auto 1fr; gap: 24px; align-items: start;
  }}
  .readiness-left {{
    display: flex; flex-direction: column; align-items: center; gap: 8px; min-width: 100px;
  }}
  .readiness-gauge {{ position: relative; width: 100px; height: 100px; }}
  .readiness-gauge canvas {{ width: 100px !important; height: 100px !important; }}
  .readiness-pct {{
    position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    font-size: 22px; font-weight: 700;
  }}
  .readiness-label {{
    font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;
    font-weight: 600; padding: 3px 10px; border-radius: 4px;
  }}

  /* Time hero */
  .time-hero {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
    padding: 20px 24px; margin-bottom: 24px;
  }}
  .time-hero-metrics {{
    display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; margin-bottom: 16px;
  }}
  .time-metric .label {{
    font-size: 11px; color: var(--text-dim); text-transform: uppercase;
    letter-spacing: 0.5px; margin-bottom: 4px;
  }}
  .time-metric .value {{
    font-size: 24px; font-weight: 700; font-variant-numeric: tabular-nums;
  }}
  .time-metric .sub {{ font-size: 11px; color: var(--text-dim); margin-top: 2px; }}
  .time-hero canvas {{ width: 100%; max-height: 160px; }}

  /* Instance cards */
  .inst-grid {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 24px;
  }}
  .inst-card {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
    padding: 20px; text-decoration: none !important; color: var(--text);
    transition: border-color 0.2s, transform 0.15s; display: flex; flex-direction: column; gap: 12px;
  }}
  .inst-card:hover {{ border-color: var(--accent); transform: translateY(-2px); }}
  .inst-header {{ display: flex; justify-content: space-between; align-items: center; }}
  .inst-header h3 {{ font-size: 18px; font-weight: 600; }}
  .inst-status {{
    font-size: 10px; text-transform: uppercase; letter-spacing: 0.6px;
    font-weight: 600; padding: 2px 8px; border-radius: 3px;
  }}
  .inst-metrics {{ display: flex; gap: 20px; flex-wrap: wrap; }}
  .inst-metric {{ text-align: center; }}
  .inst-metric-val {{ font-size: 18px; font-weight: 700; font-variant-numeric: tabular-nums; }}
  .inst-metric-label {{ font-size: 10px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.4px; }}
  .inst-areas {{ font-size: 12px; color: var(--text-dim); }}
  .inst-arrow {{ font-size: 12px; color: var(--border); transition: color 0.15s; align-self: flex-end; }}
  .inst-card:hover .inst-arrow {{ color: var(--accent); }}

  /* Charts */
  .charts {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 24px;
  }}
  .chart-box {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 20px;
  }}
  .chart-box h3 {{
    font-size: 14px; font-weight: 600; margin-bottom: 14px; color: var(--text-dim);
  }}
  .chart-box canvas {{ max-height: 260px; }}
  .wide {{ grid-column: 1 / -1; }}

  /* Info icons */
  .info-icon {{
    display: inline-flex; align-items: center; justify-content: center;
    width: 14px; height: 14px; border-radius: 50%;
    border: 1px solid var(--text-dim); font-size: 9px; font-weight: 600;
    font-style: italic; font-family: Georgia, serif;
    color: var(--text-dim); cursor: pointer; margin-left: 6px;
    transition: color 0.15s, border-color 0.15s; position: relative;
    vertical-align: middle; line-height: 1;
  }}
  .info-icon:hover {{ color: var(--accent); border-color: var(--accent); }}
  .info-tooltip {{
    position: absolute; bottom: calc(100% + 8px); left: 50%; transform: translateX(-50%);
    background: #252836; border: 1px solid var(--border); border-radius: 8px;
    padding: 10px 14px; font-size: 12px; line-height: 1.5; color: var(--text-dim);
    width: 280px; z-index: 50; box-shadow: 0 4px 16px rgba(0,0,0,0.4);
    text-transform: none; letter-spacing: 0; font-weight: 400;
  }}
  .info-tooltip::after {{
    content: ''; position: absolute; top: 100%; left: 50%; transform: translateX(-50%);
    border: 6px solid transparent; border-top-color: #252836;
  }}

  /* Modal */
  .modal-overlay {{
    display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.6); z-index: 100; align-items: center; justify-content: center;
  }}
  .modal-overlay.active {{ display: flex; }}
  .modal {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
    padding: 24px; width: 90%; max-width: 600px; max-height: 80vh;
  }}
  .modal h3 {{ font-size: 16px; margin-bottom: 16px; }}
  .modal canvas {{ max-height: 300px; }}
  .modal-close {{
    float: right; background: none; border: none; color: var(--text-dim);
    font-size: 20px; cursor: pointer; padding: 0 4px;
  }}
  .modal-close:hover {{ color: var(--text); }}

  .readiness-left {{ cursor: pointer; }}
  .readiness-left:hover .readiness-gauge {{ filter: brightness(1.15); }}
  .readiness-left .expand-hint {{
    display: flex; align-items: center; gap: 4px;
    font-size: 10px; color: var(--border); transition: color 0.15s;
  }}
  .readiness-left:hover .expand-hint {{ color: var(--accent); }}

  .chart-box.clickable {{ cursor: pointer; transition: border-color 0.15s; }}
  .chart-box.clickable:hover {{ border-color: var(--accent); }}

  .footer {{
    text-align: center; padding: 24px; font-size: 12px; color: var(--text-dim);
    border-top: 1px solid var(--border); margin-top: 24px;
  }}

  @media (max-width: 768px) {{
    .charts, .inst-grid {{ grid-template-columns: 1fr; }}
    .time-hero-metrics {{ grid-template-columns: repeat(3, 1fr); }}
    .readiness {{ grid-template-columns: 1fr; text-align: center; }}
  }}
</style>
</head>
<body>

<div class="header">
  <div>
    <h1>Meridian — Consolidated Readiness</h1>
    <div class="subtitle">
      <span>{len(instances)} instances</span>
      <span class="status-badge" style="background: {status_bg}; color: {status_color};">{status}</span>
    </div>
  </div>
  <div style="text-align: right">
    <div class="nav"><a href="index.html">&#8592; Admin Home</a></div>
    <div class="updated">Generated {now}</div>
  </div>
</div>

<!-- Readiness banner -->
<div class="readiness">
  <div class="readiness-left" onclick="showModal('domainpct')">
    <div class="readiness-gauge">
      <canvas id="readinessGauge"></canvas>
      <div class="readiness-pct" style="color: {pct_color}">{domain_pct}%</div>
    </div>
    <span class="readiness-label" style="background: {status_bg}; color: {status_color};">{status}</span>
    <div class="expand-hint">&#8599; click to expand</div>
  </div>
  <div class="readiness-right">
    <h2 style="font-size: 16px; font-weight: 600; margin-bottom: 12px;">Cross-Instance Domain Time</h2>
    <div style="font-size: 13px; color: var(--text-dim); line-height: 1.6;">
      Combined domain time across all Meridian instances. Measures how much
      of total effort goes toward domain work (client engagements, content,
      areas of responsibility) versus Meridian infrastructure (protocols,
      observations, governance). Target: 80%+ to exit prototype phase.
    </div>
  </div>
</div>

<!-- Time hero -->
<div class="time-hero">
  <div class="time-hero-metrics">
    <div class="time-metric">
      <div class="label">Total Time<span class="info-icon" onclick="showInfo(this, 'Combined time across all Meridian instances. Includes both domain work and infrastructure investment. Derived from session-activity-log.md in each instance.')" title="About">i</span></div>
      <div class="value">{fmt_hours(total_min)}</div>
      <div class="sub">{total_days} days, {total_sessions} sessions</div>
    </div>
    <div class="time-metric">
      <div class="label">Domain Time<span class="info-icon" onclick="showInfo(this, 'Time spent on actual domain work: client engagements, content creation, areas of responsibility. Allocated proportionally based on file-change ratios per session.')" title="About">i</span></div>
      <div class="value" style="color: var(--domain)">{fmt_hours(total_domain_min)}</div>
      <div class="sub">{domain_pct}% of total</div>
    </div>
    <div class="time-metric">
      <div class="label">Infra Time<span class="info-icon" onclick="showInfo(this, 'Time spent building and maintaining Meridian itself: protocols, observations, governance, CLAUDE.md, .kos/ files. Should decline as the system stabilizes.')" title="About">i</span></div>
      <div class="value" style="color: var(--infra)">{fmt_hours(total_infra_min)}</div>
      <div class="sub">{100 - domain_pct}% of total</div>
    </div>
    <div class="time-metric">
      <div class="label">Sessions<span class="info-icon" onclick="showInfo(this, 'Total Claude Code sessions across all instances. Each session is one worktree or branch conversation. Higher throughput means more gets done but also more context switches.')" title="About">i</span></div>
      <div class="value">{total_sessions}</div>
      <div class="sub">{round(total_sessions / total_days, 1) if total_days else 0} / day</div>
    </div>
    <div class="time-metric">
      <div class="label">Observations<span class="info-icon" onclick="showInfo(this, 'Meridian observations (MO entries) logged across all instances. Gaps, pattern validations, and feature candidates surfaced during real work. High volume during build phase is expected.')" title="About">i</span></div>
      <div class="value" style="color: #fb7185">{total_obs}</div>
      <div class="sub">{round(total_obs / total_days, 1) if total_days else 0} / day</div>
    </div>
  </div>
  <canvas id="timeHeroChart"></canvas>
</div>

<!-- Instance cards -->
<div class="inst-grid">
{inst_cards_html}
</div>

<!-- Charts -->
<div class="charts">
  <div class="chart-box wide">
    <h3>Combined Time Allocation: Domain vs Infrastructure (hours/day)<span class="info-icon" onclick="showInfo(this, 'Stacked bar showing how each day\\'s total time splits between domain work (green) and Meridian infrastructure (purple). Healthy trend: green grows, purple shrinks.')" title="About">i</span></h3>
    <canvas id="timeAllocChart"></canvas>
  </div>

  <div class="chart-box">
    <h3>Domain Time % by Instance<span class="info-icon" onclick="showInfo(this, 'Per-instance domain time percentage over time. Shows which instance is maturing faster and whether protocol stabilization in one instance transfers to the other. 80% target line marks operational readiness.')" title="About">i</span></h3>
    <canvas id="instCompareChart"></canvas>
  </div>

  <div class="chart-box clickable" onclick="showModal('donut')">
    <h3>Cumulative Allocation by Instance<span class="info-icon" onclick="event.stopPropagation(); showInfo(this, 'How total time breaks down: domain vs. infrastructure for each instance. Shows which instance consumes more infrastructure time and where domain effort concentrates. Click to expand.')" title="About">i</span></h3>
    <canvas id="donutChart"></canvas>
  </div>

  <div class="chart-box">
    <h3>Combined Domain % Trend<span class="info-icon" onclick="showInfo(this, 'Rolling combined domain percentage across all instances. The single most important metric for prototype exit. Must sustain above 80% to transition from Prototype to Operational.')" title="About">i</span></h3>
    <canvas id="domainPctChart"></canvas>
  </div>

  <div class="chart-box">
    <h3>Time by Instance (hours/day)<span class="info-icon" onclick="showInfo(this, 'How total daily effort distributes across instances. Shows where attention is concentrated and whether both instances are receiving active use.')" title="About">i</span></h3>
    <canvas id="instHoursChart"></canvas>
  </div>
</div>

<!-- Modal for drill-down -->
<div class="modal-overlay" id="modalOverlay" onclick="closeModal(event)">
  <div class="modal">
    <button class="modal-close" onclick="document.getElementById('modalOverlay').classList.remove('active')">&times;</button>
    <h3 id="modalTitle"></h3>
    <canvas id="modalChart"></canvas>
  </div>
</div>

<div class="footer">
  Meridian Consolidated Readiness &middot; <a href="index.html">Admin Home</a>
</div>

<script>
const labels = {date_labels};
const scaleDefaults = {{
  x: {{ ticks: {{ color: '#8888a0', font: {{ size: 11 }} }}, grid: {{ color: 'rgba(42,45,58,0.6)' }} }},
  y: {{ ticks: {{ color: '#8888a0', font: {{ size: 11 }}, callback: v => v + 'h' }}, grid: {{ color: 'rgba(42,45,58,0.6)' }}, beginAtZero: true }}
}};

// Readiness gauge
new Chart(document.getElementById('readinessGauge'), {{
  type: 'doughnut',
  data: {{ datasets: [{{ data: [{domain_pct}, {100 - domain_pct}],
    backgroundColor: ['{gauge_color}', 'rgba(42,45,58,0.4)'], borderWidth: 0 }}] }},
  options: {{ responsive: false, cutout: '75%', plugins: {{ legend: {{ display: false }}, tooltip: {{ enabled: false }} }} }}
}});

// Time hero: combined lines
new Chart(document.getElementById('timeHeroChart'), {{
  type: 'line',
  data: {{
    labels: labels,
    datasets: [
      {{ label: 'Total', data: {merged_total_hrs}, borderColor: '#e0e0e8', backgroundColor: 'rgba(224,224,232,0.05)', fill: true, tension: 0.3, pointRadius: 3, pointBackgroundColor: '#e0e0e8', borderWidth: 2.5 }},
      {{ label: 'Domain', data: {merged_domain_hrs}, borderColor: '#4ade80', backgroundColor: 'rgba(74,222,128,0.08)', fill: true, tension: 0.3, pointRadius: 3, pointBackgroundColor: '#4ade80', borderWidth: 2.5 }},
      {{ label: 'Infrastructure', data: {merged_infra_hrs}, borderColor: '#818cf8', backgroundColor: 'rgba(129,140,248,0.08)', fill: true, tension: 0.3, pointRadius: 3, pointBackgroundColor: '#818cf8', borderWidth: 2.5 }}
    ]
  }},
  options: {{
    responsive: true, maintainAspectRatio: false,
    plugins: {{
      legend: {{ labels: {{ color: '#8888a0', font: {{ size: 11 }}, usePointStyle: true, pointStyle: 'circle' }} }},
      tooltip: {{ callbacks: {{ label: ctx => ctx.dataset.label + ': ' + ctx.parsed.y.toFixed(1) + 'h' }} }}
    }},
    scales: scaleDefaults
  }}
}});

// Time allocation stacked bar
new Chart(document.getElementById('timeAllocChart'), {{
  type: 'bar',
  data: {{
    labels: labels,
    datasets: [
      {{ label: 'Domain', data: {merged_domain_hrs}, backgroundColor: 'rgba(74,222,128,0.7)', borderRadius: 4 }},
      {{ label: 'Infrastructure', data: {merged_infra_hrs}, backgroundColor: 'rgba(129,140,248,0.7)', borderRadius: 4 }}
    ]
  }},
  options: {{
    responsive: true, maintainAspectRatio: false,
    plugins: {{
      legend: {{ labels: {{ color: '#8888a0', font: {{ size: 11 }} }} }},
      tooltip: {{ callbacks: {{ label: ctx => ctx.dataset.label + ': ' + ctx.parsed.y.toFixed(1) + 'h' }} }}
    }},
    scales: {{
      x: {{ ...scaleDefaults.x, stacked: true }},
      y: {{ ...scaleDefaults.y, stacked: true }}
    }}
  }}
}});

// Domain % by instance comparison
new Chart(document.getElementById('instCompareChart'), {{
  type: 'line',
  data: {{
    labels: labels,
    datasets: [
"""

    # Add per-instance domain % lines
    for i, inst in enumerate(instances):
        series_js = to_js_array(inst_domain_pct_series[i])
        html += f"""      {{ label: '{inst["name"]}', data: {series_js}, borderColor: '{inst["color"]}', backgroundColor: '{inst["color"]}22', fill: false, tension: 0.3, pointRadius: 4, pointBackgroundColor: '{inst["color"]}', borderWidth: 2.5, spanGaps: true }},
"""

    html += f"""      {{ label: '80% Target', data: {[80]*len(merged)}, borderColor: 'rgba(245,158,11,0.5)', borderDash: [6,4], pointRadius: 0, fill: false }}
    ]
  }},
  options: {{
    responsive: true, maintainAspectRatio: false,
    plugins: {{ legend: {{ labels: {{ color: '#8888a0', font: {{ size: 11 }} }} }} }},
    scales: {{
      x: {{ ticks: {{ color: '#8888a0', font: {{ size: 11 }} }}, grid: {{ color: 'rgba(42,45,58,0.6)' }} }},
      y: {{ min: 0, max: 100, ticks: {{ color: '#8888a0', font: {{ size: 11 }}, callback: v => v+'%' }}, grid: {{ color: 'rgba(42,45,58,0.6)' }} }}
    }}
  }}
}});

// Donut: domain + infra per instance
new Chart(document.getElementById('donutChart'), {{
  type: 'doughnut',
  data: {{
    labels: {donut_labels},
    datasets: [{{ data: {donut_data}, backgroundColor: {donut_colors}, borderWidth: 1, borderColor: '#1a1d27' }}]
  }},
  options: {{
    responsive: true, maintainAspectRatio: false,
    plugins: {{
      legend: {{ position: 'right', labels: {{ color: '#8888a0', font: {{ size: 11 }}, padding: 12 }} }},
      tooltip: {{ callbacks: {{ label: ctx => {{ var t = ctx.dataset.data.reduce((a,b)=>a+b,0); return ctx.label+': '+ctx.parsed.toFixed(1)+'h ('+Math.round(ctx.parsed/t*100)+'%)'; }} }} }}
    }}
  }}
}});

// Combined domain % trend
new Chart(document.getElementById('domainPctChart'), {{
  type: 'line',
  data: {{
    labels: labels,
    datasets: [
      {{ label: 'Combined Domain %', data: {merged_domain_pcts}, borderColor: 'rgba(74,222,128,0.9)', backgroundColor: 'rgba(74,222,128,0.1)', fill: true, tension: 0.3, pointRadius: 6, pointBackgroundColor: '#4ade80' }},
      {{ label: '80% Target', data: {[80]*len(merged)}, borderColor: 'rgba(245,158,11,0.5)', borderDash: [6,4], pointRadius: 0, fill: false }}
    ]
  }},
  options: {{
    responsive: true, maintainAspectRatio: false,
    plugins: {{ legend: {{ labels: {{ color: '#8888a0', font: {{ size: 11 }} }} }} }},
    scales: {{
      x: {{ ticks: {{ color: '#8888a0', font: {{ size: 11 }} }}, grid: {{ color: 'rgba(42,45,58,0.6)' }} }},
      y: {{ min: 0, max: 100, ticks: {{ color: '#8888a0', font: {{ size: 11 }}, callback: v => v+'%' }}, grid: {{ color: 'rgba(42,45,58,0.6)' }} }}
    }}
  }}
}});

// Time by instance stacked bar
new Chart(document.getElementById('instHoursChart'), {{
  type: 'bar',
  data: {{
    labels: labels,
    datasets: [
"""

    for i, inst in enumerate(instances):
        html += f"""      {{ label: '{inst["name"]}', data: {inst_hours_series[i]}, backgroundColor: '{inst["color"]}aa', borderRadius: 2 }},
"""

    html += f"""    ]
  }},
  options: {{
    responsive: true, maintainAspectRatio: false,
    plugins: {{
      legend: {{ labels: {{ color: '#8888a0', font: {{ size: 11 }} }} }},
      tooltip: {{ callbacks: {{ label: ctx => ctx.dataset.label + ': ' + ctx.parsed.y.toFixed(1) + 'h' }} }}
    }},
    scales: {{
      x: {{ ...scaleDefaults.x, stacked: true }},
      y: {{ ...scaleDefaults.y, stacked: true }}
    }}
  }}
}});

// Info tooltip
function showInfo(el, text) {{
  var existing = el.querySelector('.info-tooltip');
  if (existing) {{ existing.remove(); return; }}
  document.querySelectorAll('.info-tooltip').forEach(t => t.remove());
  var tip = document.createElement('div');
  tip.className = 'info-tooltip';
  tip.innerHTML = text;
  el.appendChild(tip);
  setTimeout(() => {{
    document.addEventListener('click', function handler(e) {{
      if (!el.contains(e.target)) {{ tip.remove(); document.removeEventListener('click', handler); }}
    }});
  }}, 0);
}}

// Modal drill-down
var modalChart = null;
const modalData = {{
  domainpct: {{
    title: 'Combined Domain Time % per Day',
    type: 'line',
    datasets: [
      {{ label: 'Combined Domain %', data: {merged_domain_pcts}, borderColor: '#4ade80', backgroundColor: 'rgba(74,222,128,0.15)', fill: true, tension: 0.3, pointRadius: 6, pointBackgroundColor: '#4ade80' }},
      {{ label: '80% Target', data: {[80]*len(merged)}, borderColor: 'rgba(245,158,11,0.5)', borderDash: [6,4], pointRadius: 0, fill: false }}
    ],
    yLabel: '%',
    yMax: 100
  }},
  donut: {{
    title: 'Cumulative Time Allocation by Instance',
    type: 'doughnut',
    datasets: [{{ data: {donut_data}, backgroundColor: {donut_colors}, borderWidth: 1, borderColor: '#1a1d27' }}],
    donutLabels: {donut_labels}
  }}
}};

function showModal(key) {{
  var d = modalData[key];
  document.getElementById('modalTitle').textContent = d.title;
  document.getElementById('modalOverlay').classList.add('active');
  if (modalChart) modalChart.destroy();
  if (d.type === 'doughnut') {{
    modalChart = new Chart(document.getElementById('modalChart'), {{
      type: 'doughnut',
      data: {{ labels: d.donutLabels, datasets: d.datasets }},
      options: {{
        responsive: true, maintainAspectRatio: false,
        plugins: {{
          legend: {{ position: 'right', labels: {{ color: '#8888a0', font: {{ size: 12 }}, padding: 14 }} }},
          tooltip: {{ callbacks: {{ label: ctx => {{ var t = ctx.dataset.data.reduce((a,b)=>a+b,0); return ctx.label+': '+ctx.parsed.toFixed(1)+'h ('+Math.round(ctx.parsed/t*100)+'%)'; }} }} }}
        }}
      }}
    }});
  }} else {{
    modalChart = new Chart(document.getElementById('modalChart'), {{
      type: 'line',
      data: {{ labels: labels, datasets: d.datasets }},
      options: {{
        responsive: true, maintainAspectRatio: false,
        plugins: {{ legend: {{ labels: {{ color: '#8888a0' }} }} }},
        scales: {{
          x: {{ ticks: {{ color: '#8888a0' }}, grid: {{ color: 'rgba(42,45,58,0.6)' }} }},
          y: {{ beginAtZero: true, max: d.yMax || undefined, ticks: {{ color: '#8888a0', callback: v => v + (d.yLabel || '') }}, grid: {{ color: 'rgba(42,45,58,0.6)' }} }}
        }}
      }}
    }});
  }}
}}

function closeModal(e) {{
  if (e.target === document.getElementById('modalOverlay')) {{
    document.getElementById('modalOverlay').classList.remove('active');
  }}
}}
</script>
</body>
</html>"""

    return html


def main():
    instances = []
    for inst_config in INSTANCES:
        if inst_config["log"].exists():
            data = parse_instance(inst_config)
            instances.append(data)
            print(f"  {data['name']}: {data['total_sessions']} sessions across {data['days']} days ({data['domain_pct']}% domain)")
        else:
            print(f"  {inst_config['name']}: log not found at {inst_config['log']}, skipping")

    if not instances:
        print("No instance data found. Exiting.")
        return

    merged = merge_daily(instances)
    html = generate_html(instances, merged)
    OUTPUT_FILE.write_text(html)
    print(f"Consolidated dashboard generated: {OUTPUT_FILE}")
    print(f"  Open with: open {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
