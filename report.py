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
# SESSION
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "subject" not in st.session_state:
    st.session_state.subject = ""

# =====================================================
# CSS
# =====================================================

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

html,body,[class*="css"]{
    font-family:'Manrope',sans-serif;
}

.block-container{
    max-width:1200px;
    padding-top:2rem;
    padding-bottom:2rem;
}

.report-title{
    text-align:center;
    font-size:70px;
    font-weight:800;
    color:#111111;
    margin-bottom:0;
}

.report-subtitle{
    text-align:center;
    font-size:30px;
    font-weight:700;
    color:#2E7D32;
    margin-top:-10px;
}

.report-desc{
    text-align:center;
    color:#666666;
    font-size:18px;
    margin-bottom:45px;
}

/* CARD */

.subject-card{

    background:white;

    border:1px solid #E8F5E9;

    border-radius:22px;

    padding:28px;

    min-height:240px;

    box-shadow:0px 8px 18px rgba(0,0,0,.05);

}

.subject-title{

    font-size:30px;

    font-weight:800;

    color:#111111;

}

.subject-sub{

    font-size:18px;

    color:#555;

    margin-top:12px;

}

.subject-file{

    margin-top:20px;

    color:#2E7D32;

    font-weight:700;

}

hr{

border:none;

border-top:1px solid #E8F5E9;

margin-top:20px;

margin-bottom:20px;

}

.stButton>button{

width:100%;

background:#2E7D32;

color:white;

border:none;

border-radius:12px;

height:48px;

font-size:17px;

font-weight:700;

}

.stButton>button:hover{

background:#215d25;

color:#E8F5E9;

}

</style>

""", unsafe_allow_html=True)


# =====================================================
# NAVIGATION
# =====================================================

def goto_subject(name):

    st.session_state.subject = name

    st.session_state.page = "subject"

    st.rerun()


def goto_home():

    st.session_state.page = "home"

    st.rerun()
    # =====================================================
# HOME PAGE
# =====================================================

def home_page():

    st.markdown(
        """
        <div class="report-title">
            REPORT
        </div>

        <div class="report-subtitle">
            Cannabis EEG Classification Research Portal
        </div>

        <div class="report-desc">
            Choose one of the available experimental reports.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ===========================
    # SUBJECT 1 & SUBJECT 10
    # ===========================

    col1, col2 = st.columns(2, gap="large")

    with col1:

        with st.container(border=True):

            st.markdown(
                """
                <div class="subject-title">
                Subject 1
                </div>

                <div class="subject-sub">
                Single Subject Analysis
                </div>

                <div class="subject-file">
                40 EEG CSV Files
                </div>

                <hr>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Explore Report →",
                key="subject1"
            ):
                goto_subject("Subject 1")

    with col2:

        with st.container(border=True):

            st.markdown(
                """
                <div class="subject-title">
                Subject 10
                </div>

                <div class="subject-sub">
                Multi Subject Analysis
                </div>

                <div class="subject-file">
                400 EEG CSV Files
                </div>

                <hr>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Explore Report →",
                key="subject10"
            ):
                goto_subject("Subject 10")

    st.write("")
    st.write("")

    # ===========================
    # SUBJECT 30 & FUTURE
    # ===========================

    col3, col4 = st.columns(2, gap="large")

    with col3:

        with st.container(border=True):

            st.markdown(
                """
                <div class="subject-title">
                Subject 30
                </div>

                <div class="subject-sub">
                Large Scale Analysis
                </div>

                <div class="subject-file">
                1200 EEG CSV Files
                </div>

                <hr>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Explore Report →",
                key="subject30"
            ):
                goto_subject("Subject 30")

    with col4:

        with st.container(border=True):

            st.markdown(
                """
                <div class="subject-title">
                Future Subject
                </div>

                <div class="subject-sub">
                Coming Soon
                </div>

                <div class="subject-file">
                Reserved for future experiments
                </div>

                <hr>
                """,
                unsafe_allow_html=True
            )

            st.button(
                "Coming Soon",
                disabled=True,
                key="future"
            )
            # =====================================================
# SUBJECT PAGE (Placeholder)
# =====================================================

def subject_page():

    # Tombol kembali
    if st.button("← Back to Reports"):
        goto_home()

    st.write("")

    st.markdown(f"""
    <h1 style='color:#111111; margin-bottom:0;'>
        {st.session_state.subject}
    </h1>

    <p style='color:#2E7D32; font-size:20px; margin-top:5px;'>
        Cannabis EEG Classification using
        Auxiliary Classifier Generative Adversarial Network (ACGAN)
    </p>

    <hr>
    """, unsafe_allow_html=True)

    st.info(
        "This page is under development.\n\n"
        "The following sections will be added:\n"
        "- Overview\n"
        "- Dataset\n"
        "- Preprocessing\n"
        "- ACGAN\n"
        "- Models\n"
        "- Results\n"
        "- Paper"
    )


# =====================================================
# ROUTER
# =====================================================

if st.session_state.page == "home":
    home_page()

elif st.session_state.page == "subject":
    subject_page()
