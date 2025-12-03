import streamlit as st

from racecontrolClient import (
    get_completed_round,
    get_schedule,
    get_driver_standings,
    get_constructor_standings,
    get_all_results_up_to,
    get_fantasy_scores,
)

from racecontrolCore.ui.layout import render_header, render_kpis, render_tabs
from racecontrolCore.services.state import (
    init_session_flags,
    set_offline,
    clear_offline,
)
from racecontrolCore.utils import format_next_race_when


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="RaceControl Dashboard",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session_flags()

# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ Controls")

season = st.sidebar.text_input("Season", value="2025")

last_n = st.sidebar.slider(
    "Last N rounds for form",
    min_value=2, max_value=10, value=5, step=1
)

w_recent = st.sidebar.slider(
    "Weight – Recent form",
    min_value=0.0, max_value=1.0, value=0.7, step=0.05
)

w_season = st.sidebar.slider(
    "Weight – Season form",
    min_value=0.0, max_value=1.0, value=0.3, step=0.05
)

vol_penalty = st.sidebar.slider(
    "Volatility penalty",
    min_value=0.0, max_value=1.0, value=0.2, step=0.05
)

show_per_race = st.sidebar.checkbox("Show per-race details", value=False)

if st.sidebar.button("🔁 Refresh"):
    clear_offline()
    st.rerun()


# ---------- DATA FETCH ----------
try:
    completed_round = get_completed_round(season)
    schedule_rows = get_schedule(season)
    drivers = get_driver_standings(season)
    teams = get_constructor_standings(season)
    results = get_all_results_up_to(season, completed_round)

    # Compute total number of races from schedule
    total_races = max(
        (row.get("round", 0) for row in schedule_rows),
        default=0
    )

    # Determine next race
    next_race_name = ""
    next_race_when = None

    target_round = completed_round + 1

    for row in schedule_rows:
        if row.get("round") == target_round:
            next_race_name = row.get("name", "")
            next_race_when = format_next_race_when(row.get("local_date"))
            break

    if not next_race_name and completed_round >= total_races:
        next_race_name = "Season Complete"

    fantasy_scores = get_fantasy_scores(
        season=season,
        round_inclusive=completed_round,
        last_n=last_n,
        w_recent=w_recent,
        w_season=w_season,
        vol_penalty=vol_penalty,
    )

except Exception as e:
    set_offline(str(e))
    completed_round = 0
    total_races = 0
    next_race_name = ""
    next_race_when = None
    schedule_rows = []
    drivers = []
    teams = []
    results = []
    fantasy_scores = []


# ---------- RENDER UI ----------
title = f"RaceControl — {season}"
render_header(title, "Live F1 Data Powered by Jolpica")

render_kpis(
    completed_round=completed_round,
    total_races=total_races,
    next_race_name=next_race_name,
    next_race_when=next_race_when,
    drivers=drivers,
    teams=teams,
)

render_tabs(
    drivers=drivers,
    teams=teams,
    results=results,
    fantasy_scores=fantasy_scores,
    show_per_race=show_per_race,
)