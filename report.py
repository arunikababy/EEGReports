import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Cannabis EEG Research Portal",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# COLOR
# =====================================================

GREEN = "#2E7D32"
LIGHT = "#E8F5E9"

# =====================================================
# CSS
# =====================================================

st.markdown(f"""
<style>

#MainMenu{{visibility:hidden;}}
footer{{visibility:hidden;}}
header{{visibility:hidden;}}

.block-container{{
    max-width:1200px;
    padding-top:2rem;
}}

h1,h2,h3,p{{
    color:black;
}}

.report-title{{
    text-align:center;
    font-size:64px;
    font-weight:800;
    margin-bottom:5px;
}}

.report-subtitle{{
    text-align:center;
    color:{GREEN};
    font-size:28px;
    font-weight:600;
}}

.report-desc{{
    text-align:center;
    color:#666;
    font-size:18px;
    margin-bottom:50px;
}}

div[data-testid="stVerticalBlockBorderWrapper"]{{
    border:1px solid {LIGHT};
    border-radius:18px;
    padding:20px;
    box-shadow:0px 6px 16px rgba(0,0,0,.05);
    transition:0.3s;
}}

div[data-testid="stVerticalBlockBorderWrapper"]:hover{{
    border:1px solid {GREEN};
    transform:translateY(-4px);
}}

.stButton>button{{
    width:100%;
    background:{GREEN};
    color:white;
    border:none;
    border-radius:10px;
    height:45px;
    font-weight:600;
}}

.stButton>button:hover{{
    background:#256428;
    color:white;
}}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown(
"""
<div class="report-title">
REPORT
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="report-subtitle">
Cannabis EEG Classification Research Portal
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="report-desc">
Choose one of the available experimental reports.
</div>
""",
unsafe_allow_html=True
)

# =====================================================
# FUNCTION
# =====================================================

def subject_card(title, subtitle, files, key):

    with st.container(border=True):

        st.markdown(f"## {title}")

        st.write(subtitle)

        st.caption(files)

        st.write("")

        if st.button("Explore Report →", key=key):

            st.session_state.subject = title

            st.switch_page("pages/report.py")


# =====================================================
# GRID
# =====================================================

col1,col2=st.columns(2,gap="large")

with col1:

    subject_card(
        "Subject 1",
        "Single Subject Analysis",
        "40 EEG CSV Files",
        "s1"
    )

with col2:

    subject_card(
        "Subject 10",
        "Multi Subject Analysis",
        "400 EEG CSV Files",
        "s10"
    )

st.write("")

col3,col4=st.columns(2,gap="large")

with col3:

    subject_card(
        "Subject 30",
        "Large Scale Analysis",
        "1200 EEG CSV Files",
        "s30"
    )

with col4:

    with st.container(border=True):

        st.markdown("## Future Subject")

        st.write("Coming Soon")

        st.caption("Reserved for future experiment")

        st.button(
            "Coming Soon",
            disabled=True,
            use_container_width=True
        )
