import streamlit as st
from scripts import parser, scorer, suggester, formatter, ocr_reader, linkedin_scraper, report_generator
from utils import config, helpers
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="ResuMate AI", layout="wide")

col1, col2 = st.columns([1, 8])
with col1:
    st.image("assets/logo.jpeg", width=100)
with col2:
    st.markdown("<h1 style='margin-top: 10px;'>ResuMate AI - Smart Resume Analyzer</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Upload Resume & JD",
    "ATS Score Report",
    "Suggestions",
    "LinkedIn Analyzer",
    "Charts",
    "Export PDF"
])

with tab1:
    st.header("📤 Upload Resume and Job Description")
    resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
    jd_text = st.text_area("Paste Job Description")
    if st.button("Analyze"):
        if resume_file and jd_text.strip():
            resume_text = parser.parse_resume(resume_file)
            jd_keywords = parser.extract_keywords(jd_text)
            st.session_state.resume_text = resume_text
            st.session_state.jd_keywords = jd_keywords
            st.success("Resume and JD parsed successfully!")
        else:
            st.warning("Please upload a resume and paste the job description.")

with tab2:
    st.header("🎯 ATS Score & Matching")
    if "resume_text" in st.session_state and "jd_keywords" in st.session_state:
        score_data = scorer.calculate_score(st.session_state.resume_text, st.session_state.jd_keywords)
        st.metric("ATS Score", f"{score_data['ats_score']} / 100")
        st.subheader("✅ Matched Skills")
        st.write(score_data['matched'])
        st.subheader("❌ Missing Keywords")
        st.write(score_data['missing'])
    else:
        st.warning("Please upload and analyze resume first.")

with tab3:
    st.header("💡 Suggestions")
    if "resume_text" in st.session_state and "jd_keywords" in st.session_state:
        suggestions = suggester.get_suggestions(st.session_state.resume_text, st.session_state.jd_keywords)
        st.write(suggestions)
    else:
        st.warning("Please upload and analyze resume first.")

with tab4:
    st.header("🔗 LinkedIn Profile Analyzer")
    linkedin_url = st.text_input("Paste LinkedIn Profile URL")
    if st.button("Analyze LinkedIn"):
        if linkedin_url.strip():
            content = linkedin_scraper.scrape(linkedin_url)
            st.text_area("Extracted Content", content)
        else:
            st.warning("Please enter a valid LinkedIn profile URL.")

with tab5:
    st.header("📊 Score Breakdown")
    if "resume_text" in st.session_state:
        scorer.show_charts()
    else:
        st.warning("Upload resume first.")

with tab6:
    st.header("⬇️ Export ATS Report")
    if st.button("Download PDF"):
        if "resume_text" in st.session_state and "jd_keywords" in st.session_state:
            score_data = scorer.calculate_score(st.session_state.resume_text, st.session_state.jd_keywords)
            report_path = report_generator.generate_pdf(score_data)
            with open(report_path, "rb") as file:
                st.download_button("Download Report", file, file_name="ATS_Report.pdf")
        else:
            st.warning("Please analyze the resume before exporting the report.")
