import streamlit as st

def init_session_flags():
    if "offline" not in st.session_state:
        st.session_state["offline"] = False
    if "last_error" not in st.session_state:
        st.session_state["last_error"] = ""

def set_offline(err: str | None = None):
    st.session_state["offline"] = True
    if err:
        st.session_state["last_error"] = err

def clear_offline():
    st.session_state["offline"] = False
    st.session_state["last_error"] = ""

def get_offline_state() -> tuple[bool, str]:
    return (
        bool(st.session_state.get("offline", False)),
        str(st.session_state.get("last_error", "")),
    )