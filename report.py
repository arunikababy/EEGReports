import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Cannabis EEG Report",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# SESSION
# ==========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "subject" not in st.session_state:
    st.session_state.subject = ""

# ==========================================================
# COLOR
# ==========================================================

WHITE = "#FFFFFF"
BLACK = "#111111"
GREEN = "#2E7D32"
LIGHT = "#E8F5E9"

# ==========================================================
# CSS
# ==========================================================

st.markdown(f"""

<style>

#MainMenu{{visibility:hidden;}}

footer{{visibility:hidden;}}

header{{visibility:hidden;}}

.block-container{{
    padding-top:2rem;
    max-width:1250px;
}}

html,body,[class*="css"]{{
    font-family:'Segoe UI',sans-serif;
}}

.hero{{
    text-align:center;
    margin-top:20px;
    margin-bottom:60px;
}}

.hero h1{{
    font-size:72px;
    color:{BLACK};
    margin-bottom:5px;
}}

.hero h3{{
    color:{GREEN};
    font-weight:500;
}}

.hero p{{
    color:#666;
    font-size:18px;
}}

.subject-card{{
    background:white;
    border-radius:20px;
    padding:30px;
    border:1px solid {LIGHT};
    box-shadow:0px 8px 18px rgba(0,0,0,.05);
    text-align:center;
}}

.subject-title{{
    font-size:30px;
    font-weight:700;
    color:{BLACK};
}}

.subject-desc{{
    color:#666;
}}

</style>

""",unsafe_allow_html=True)

# ==========================================================
# FUNCTION
# ==========================================================

def open_subject(subject):

    st.session_state.subject=subject

    st.session_state.page="subject"

    st.rerun()
