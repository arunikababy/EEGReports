import streamlit as st

st.set_page_config(
    page_title="Cannabis EEG Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# LOAD CSS
# ============================================================

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ============================================================
# NAVBAR
# ============================================================

col1,col2,col3=st.columns([1,6,1])

with col1:

    st.image("assets/logo.png",width=70)

with col2:

    st.markdown(
        "<h2 class='logo-text'>EEG ACGAN Dashboard</h2>",
        unsafe_allow_html=True
    )

with col3:

    st.button("📄 Paper")

st.divider()

# ============================================================
# MENU
# ============================================================

menu=[
    "Overview",
    "Dataset",
    "Preprocessing",
    "ACGAN",
    "Models",
    "Results",
    "About"
]

selected=st.segmented_control(

    "",

    menu,

    default="Overview"

)

st.write("")

# ============================================================
# HERO
# ============================================================

left,right=st.columns([1.2,1])

with left:

    st.markdown("""
    <div class="hero-title">

    Cannabis Classification Using

    <span>

    Auxiliary Classifier GAN (ACGAN)

    </span>

    </div>

    """,unsafe_allow_html=True)

    st.markdown("""

    <div class="hero-subtitle">

    Single Subject Cannabis EEG Analysis

    <br>

    <b>Eye Closed</b> vs <b>Flanker Task</b>

    </div>

    """,unsafe_allow_html=True)

    st.write("")

    c1,c2=st.columns([1,1])

    with c1:

        st.button(
            "Explore Results",
            use_container_width=True
        )

    with c2:

        st.button(
            "Learn More",
            use_container_width=True
        )

with right:

    st.image(
        "assets/hero.png",
        use_container_width=True
    )

st.write("")
st.write("")

# ============================================================
# METRIC CARDS
# ============================================================

a,b,c,d,e=st.columns(5)

a.metric(
    "EEG Files",
    "40"
)

b.metric(
    "Subjects",
    "1"
)

c.metric(
    "Classes",
    "4"
)

d.metric(
    "Models",
    "3"
)

e.metric(
    "Best Accuracy",
    "98.25%"
)

st.write("")
st.divider()
