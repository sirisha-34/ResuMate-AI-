import os

# Tesseract OCR path (update if installed elsewhere)
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Supported file extensions
RESUME_EXTENSIONS = [".pdf", ".docx"]
JD_EXTENSIONS = [".txt"]

# OpenAI model (if used)
OPENAI_MODEL = "gpt-3.5-turbo"

# Directory paths
DATA_DIR = "data"
OUTPUT_DIR = "outputs"
TEMPLATE_PATH = "templates/ats_report_template.html"

# Ensure required folders exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Keywords for scoring resumes (can be expanded)
KEYWORDS = [
    "python", "java", "sql", "machine learning", "deep learning",
    "data analysis", "communication", "teamwork", "leadership",
    "problem-solving", "time management", "project management"
]

# Section weights for overall score calculation
WEIGHTS = {
    "skills": 0.4,
    "experience": 0.3,
    "education": 0.2,
    "projects": 0.1
}
