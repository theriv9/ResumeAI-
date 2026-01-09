import streamlit as st

st.set_page_config(
    page_title="Resume Keyword Extractor",
    page_icon="🔍",
    layout="centered"
)

st.title("Resume Keyword Extractor")

st.markdown("Paste the **full job description** below:")

job_description = st.text_area(
    label="Job Description",
    height=300,
    placeholder="Example:\nWe are looking for a Senior Python Developer with experience in Streamlit, Azure OpenAI, LangChain, and cloud deployment...",
    help="Copy and paste the entire job posting here (no need to upload files yet)"
)

# Tiny feedback line (shows it's ready for next step)
if job_description.strip():
    st.info("Job description received — ready for keyword extraction!")
else:
    st.info("Waiting for the job description...")