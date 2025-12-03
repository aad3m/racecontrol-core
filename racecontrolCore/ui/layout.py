import streamlit as st
import plotly.express as px

from racecontrolCore.services.state import get_offline_state

def _css():
    st.markdown(
        """
        <style>
        .block-container { padding-top: 1.2rem; }
        [data-testid="stMetricValue"] { font-size: 1.6rem; }
        .kpi-card {
            border:1px solid rgba(128,128,128,0.2);
            border-radius:16px;
            padding:14px 16px;
            background: rgba(127,127,127,0.07);
            backdrop-filter: blur(6px);
        }
        .section-card {
            border:1px solid rgba(128,128,128,0.2);
            border-radius:16px;
            padding:16px 18px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def render_header(title: str, caption: str):
    _css()
    st.title(f"🏁 {title}")
    st.caption(caption)

    offline, last_error = get_offline_state()
    if offline:
        st.warning(
            "Network issue or API unreachable. You're in **Offline Mode**. "
            "Some charts/tables may be empty.\n\n"
            f"Last error: `{last_error}`"
        )

def render_kpis(
    completed_round: int,
    total_races: int,
    next_race_name: str,
    next_race_when: str | None,
    drivers: list[dict],
    teams: list[dict],
):
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
        st.metric("Completed Rounds", completed_round, f"of {total_races}")
        st.markdown("</div>", unsafe_allow_html=True)

    with k2:
        st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
        if drivers:
            leader = sorted(drivers, key=lambda d: d.get("position", 9999))[0]
            st.metric(
                "Drivers’ Leader",
                leader.get("driver", "—"),
                f'{int(leader.get("points", 0))} pts',
            )
        else:
            st.metric("Drivers’ Leader", "—", "")
        st.markdown("</div>", unsafe_allow_html=True)

    with k3:
        st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
        if teams:
            leader = sorted(teams, key=lambda t: t.get("position", 9999))[0]
            st.metric(
                "Constructors’ Leader",
                leader.get("team", "—"),
                f'{int(leader.get("points", 0))} pts',
            )
        else:
            st.metric("Constructors’ Leader", "—", "")
        st.markdown("</div>", unsafe_allow_html=True)

    with k4:
        st.markdown('<div class="kpi-card">', unsafe_allow_html=True)
        if next_race_name:
            label = next_race_when or "TBA"
            st.metric("Next Race", next_race_name, label)
        else:
            st.metric("Next Race", "Season Complete", "")
        st.markdown("</div>", unsafe_allow_html=True)

def render_tabs(
    drivers: list[dict],
    teams: list[dict],
    results: list[dict],
    fantasy_scores: list[dict],
    show_per_race: bool,
):
    tab_overview, tab_drivers, tab_teams, tab_races, tab_fantasy = st.tabs(
        ["📊 Overview", "👤 Drivers", "🏎️ Teams", "🗺️ Race Tracker", "🧮 Fantasy Helper"]
    )

    with tab_overview:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.subheader("Drivers – Points")
            if drivers:
                fig = px.bar(drivers, x="driver", y="points")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No driver data.")
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.subheader("Constructors – Points")
            if teams:
                fig = px.bar(teams, x="team", y="points")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No constructor data.")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab_drivers:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("Full Driver Standings")
        st.dataframe(drivers, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_teams:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("Full Constructor Standings")
        st.dataframe(teams, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_races:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("Race Results (Up to Selected Round)")
        st.dataframe(results, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_fantasy:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("Fantasy Helper – Driver Scores")
        if fantasy_scores:
            fig = px.bar(fantasy_scores, x="driver", y="fantasy_score")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(fantasy_scores, use_container_width=True)
        else:
            st.info("No fantasy data yet. Try increasing the completed round or last N.")
        st.markdown("</div>", unsafe_allow_html=True)