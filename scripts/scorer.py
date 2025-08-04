from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.config import WEIGHTS
import matplotlib.pyplot as plt
import streamlit as st

def calculate_score(resume_text, jd_keywords):
    matched = [kw for kw in jd_keywords if kw in resume_text.lower()]
    missing = [kw for kw in jd_keywords if kw not in resume_text.lower()]
    tfidf = TfidfVectorizer().fit_transform([" ".join(jd_keywords), resume_text])
    cosine = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    score = int(cosine * 100)
    return {"ats_score": score, "matched": matched, "missing": missing}

def show_charts():
    labels = ['Skills', 'Formatting', 'Experience', 'Match']
    sizes = [60, 20, 10, 10]
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)