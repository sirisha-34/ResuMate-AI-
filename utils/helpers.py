import re
import docx2txt
import pytesseract
import pdfplumber
import cv2
import numpy as np
from PIL import Image
import nltk

# 🔽 Auto-download required NLTK data if missing
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(docx_file):
    return docx2txt.process(docx_file)

def extract_text_from_image(image_bytes):
    image = Image.open(image_bytes)
    return pytesseract.image_to_string(image)

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    return " ".join([t for t in tokens if t.isalnum() and t not in stop_words])

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()
