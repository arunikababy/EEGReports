import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Cannabis EEG Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

/* Hide Streamlit default menu & footer */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main */

.block-container{
    max-width:1200px;
    padding-top:2rem;
}

/* Navigation */

.navbar{
    display:flex;
    justify-content:center;
    gap:40px;
    margin-top:5px;
    margin-bottom:55px;
    font-weight:600;
    font-size:16px;
}

.navbar span{
    color:#222;
    cursor:pointer;
}

.navbar span:hover{
    color:#2E7D32;
}

/* Hero */

.hero-title{
    text-align:center;
    font-size:58px;
    font-weight:800;
    color:black;
    line-height:1.2;
}

.hero-green{
    color:#2E7D32;
}

.hero-subtitle{
    text-align:center;
    font-size:22px;
    color:#555;
    margin-top:18px;
    margin-bottom:35px;
}

/* Button */

div.stButton > button{
    background:#2E7D32;
    color:white;
    border-radius:14px;
    border:none;
    padding:12px 30px;
    font-size:17px;
    font-weight:600;
}

div.stButton > button:hover{
    background:#215d25;
    color:white;
}

/* Metric Card */

.metric-card{

    background:white;

    border-radius:20px;

    padding:28px;

    border:1px solid #E8F5E9;

    box-shadow:0px 6px 18px rgba(0,0,0,.06);

    text-align:center;

    transition:.3s;
}

.metric-card:hover{

    transform:translateY(-5px);

    border:1px solid #2E7D32;
}

.metric-value{

    font-size:36px;

    font-weight:800;

    color:#2E7D32;

}

.metric-title{

    color:#666;

    font-size:15px;

    margin-top:8px;

}

</style>
""", unsafe_allow_html=True)

# =====================================================
# NAVIGATION
# =====================================================

st.markdown("""
<div class="navbar">
<span>Overview</span>
<span>Dataset</span>
<span>Preprocessing</span>
<span>ACGAN</span>
<span>Results</span>
<span>Paper</span>
</div>
""", unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero-title">

Cannabis Classification Using<br>

<span class="hero-green">

Auxiliary Classifier GAN (ACGAN)

</span>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-subtitle">

Artificial Intelligence for Cannabis EEG Analysis

<br>

Eye Closed &nbsp; • &nbsp; Flanker Task

</div>
""", unsafe_allow_html=True)

c1,c2,c3=st.columns([2,1,2])

with c2:

    st.button(
        "Explore Results",
        use_container_width=True
    )

st.write("")
st.write("")

# =====================================================
# METRIC CARDS
# =====================================================

col1,col2,col3,col4,col5=st.columns(5)

cards=[

("40","EEG Files"),

("1","Subject"),

("4","Classes"),

("3","Models"),

("98.25%","Accuracy")

]

cols=[col1,col2,col3,col4,col5]

for col,(value,title) in zip(cols,cards):

    with col:

        st.markdown(f"""

        <div class="metric-card">

        <div class="metric-value">{value}</div>

        <div class="metric-title">{title}</div>

        </div>

        """,unsafe_allow_html=True)

st.write("")
st.divider()

# =====================================================
# NEXT SECTION (Placeholder)
# =====================================================

st.subheader("Research Workflow")

st.info("➡️ Tahap berikutnya akan berisi Workflow Pipeline, Dataset, dan Preprocessing.")
