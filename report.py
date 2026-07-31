import streamlit as st

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="Cannabis EEG Dashboard",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------
st.markdown("""
<style>

.main{
    background-color:white;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1300px;
}

.title{
    font-size:48px;
    font-weight:800;
    color:#111111;
    line-height:1.2;
}

.subtitle{
    font-size:20px;
    color:#2E7D32;
}

.section-title{
    color:#1B5E20;
    font-size:30px;
    font-weight:700;
    margin-top:10px;
}

.metric-card{
    background:white;
    border-radius:18px;
    padding:20px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
    border-left:6px solid #2E7D32;
}

.protocol-card{
    background:#F8FFF9;
    border-radius:20px;
    padding:18px;
    border:2px solid #A5D6A7;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown("""
<div class="title">
Cannabis Classification Using
<span style="color:#1B5E20">
Auxiliary Classifier GAN (ACGAN)
</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Single Subject Cannabis EEG Analysis<br>
Eye Closed vs Flanker Task
</div>
""", unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.title("Navigation")

protocol = st.sidebar.selectbox(
    "Protocol",
    [
        "Single Subject",
        "10 Subjects",
        "30 Subjects"
    ]
)

page = st.sidebar.radio(
    "Menu",
    [
        "Overview",
        "Dataset",
        "Preprocessing",
        "ACGAN",
        "Models",
        "Results"
    ]
)

# -------------------------------------------------------
# PROTOCOL INFO
# -------------------------------------------------------

col1,col2,col3=st.columns(3)

with col1:
    st.markdown("""
    <div class="protocol-card">
    <h3>👤 Single Subject</h3>
    40 EEG CSV Files
    </div>
    """,unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="protocol-card">
    <h3>👥 10 Subjects</h3>
    Multi Subject
    </div>
    """,unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="protocol-card">
    <h3>👥 30 Subjects</h3>
    Large Scale
    </div>
    """,unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------
# PAGE CONTENT
# -------------------------------------------------------

if page=="Overview":

    st.markdown('<div class="section-title">Overview</div>',unsafe_allow_html=True)

    st.write("""
This dashboard presents an interactive workflow for cannabis EEG
classification using Auxiliary Classifier GAN (ACGAN).
""")

    c1,c2=st.columns(2)

    with c1:

        st.success("EEG Dataset Management")

        st.success("Feature Extraction")

        st.success("ACGAN Data Augmentation")

    with c2:

        st.success("SVM")

        st.success("Random Forest")

        st.success("CNN 1D")



elif page=="Dataset":

    st.markdown('<div class="section-title">Dataset</div>',unsafe_allow_html=True)

    st.markdown("""
- BCF (Before Cannabis Oil – Eye Closed)
- ACF (After Cannabis Oil – Eye Closed)

- BF (Before Cannabis Oil – Flanker)

- AF (After Cannabis Oil – Flanker)
""")

    st.info("Total Dataset : 40 EEG CSV Files")



elif page=="Preprocessing":

    st.markdown('<div class="section-title">Preprocessing</div>',unsafe_allow_html=True)

    col1,col2=st.columns(2)

    with col1:

        st.subheader("Extracted Features")

        st.write("• Band Power")

        st.write("• Relative Power")

        st.write("• Entropy")

        st.write("• Hjorth Parameters")

    with col2:

        st.subheader("Frequency Bands")

        st.write("• Delta")

        st.write("• Theta")

        st.write("• Alpha")

        st.write("• Beta")

        st.write("• Gamma")



elif page=="ACGAN":

    st.markdown('<div class="section-title">ACGAN</div>',unsafe_allow_html=True)

    st.write("### Input")

    st.write("Feature Vector")

    st.write("### Process")

    st.write("• Train Generator")

    st.write("• Train Discriminator")

    st.write("• Generate Synthetic EEG")

    st.write("### Output")

    st.write("Synthetic BF")

    st.write("Synthetic AF")

    st.write("Synthetic BCF")

    st.write("Synthetic ACF")



elif page=="Models":

    st.markdown('<div class="section-title">Classification Models</div>',unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    c1.metric("Model 1","SVM")

    c2.metric("Model 2","Random Forest")

    c3.metric("Model 3","CNN 1D")



elif page=="Results":

    st.markdown('<div class="section-title">Experimental Results</div>',unsafe_allow_html=True)

    st.info("Upload your figures below.")

    acc=st.file_uploader(
        "Accuracy Graph",
        type=["png","jpg"]
    )

    cm=st.file_uploader(
        "Confusion Matrix",
        type=["png","jpg"]
    )

    roc=st.file_uploader(
        "ROC Curve",
        type=["png","jpg"]
    )

    if acc:
        st.image(acc,use_container_width=True)

    if cm:
        st.image(cm,use_container_width=True)

    if roc:
        st.image(roc,use_container_width=True)

st.divider()

st.caption("© 2026 Cannabis EEG Classification Dashboard | University Malaysia Perlis")
