import docx2txt
import fitz  # PyMuPDF
import re
from utils.helpers import clean_text

def parse_resume(file):
    file_name = file.name.lower()

    if file_name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = "".join(page.get_text() for page in doc)
    elif file_name.endswith(".docx"):
        text = docx2txt.process(file)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

    return clean_text(text)

def extract_keywords(jd_text):
    words = re.findall(r"\b\w+\b", jd_text.lower())
    keywords = list(set(words))  # Remove duplicates
    return keywords
