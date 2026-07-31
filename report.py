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
# ==========================================================
# HOME PAGE
# ==========================================================

def home_page():

    st.markdown("""
    <div class="hero">
        <h1>REPORT</h1>
        <h3>Cannabis EEG Classification using Auxiliary Classifier GAN (ACGAN)</h3>
        <p>
        Select one of the available research reports below.
        <br>
        Each report represents a different experimental scenario.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # -----------------------------
    # Row 1
    # -----------------------------

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("""
        <div class="subject-card">
            <div style="font-size:60px;">👤</div>
            <div class="subject-title">Subject 1</div>
            <div class="subject-desc">
                Single Subject Analysis
                <br><br>
                40 EEG CSV Files
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Explore Subject 1",
            use_container_width=True,
            key="subject1"
        ):
            open_subject("Subject 1")

    with col2:

        st.markdown("""
        <div class="subject-card">
            <div style="font-size:60px;">👥</div>
            <div class="subject-title">Subject 10</div>
            <div class="subject-desc">
                Multi Subject Analysis
                <br><br>
                400 EEG CSV Files
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Explore Subject 10",
            use_container_width=True,
            key="subject10"
        ):
            open_subject("Subject 10")

    st.write("")
    st.write("")

    # -----------------------------
    # Row 2
    # -----------------------------

    col3, col4 = st.columns(2, gap="large")

    with col3:

        st.markdown("""
        <div class="subject-card">
            <div style="font-size:60px;">👥</div>
            <div class="subject-title">Subject 30</div>
            <div class="subject-desc">
                Large Scale Analysis
                <br><br>
                1200 EEG CSV Files
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Explore Subject 30",
            use_container_width=True,
            key="subject30"
        ):
            open_subject("Subject 30")

    with col4:

        st.markdown("""
        <div class="subject-card">
            <div style="font-size:60px;">➕</div>
            <div class="subject-title">Future Subject</div>
            <div class="subject-desc">
                Reserved for future experiments.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Coming Soon",
            disabled=True,
            use_container_width=True,
            key="future"
        )
