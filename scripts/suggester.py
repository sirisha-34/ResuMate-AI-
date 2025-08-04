import os
import google.generativeai as genai
from huggingface_hub import InferenceClient
import cohere
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
COHERE_KEY = os.getenv("COHERE_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
hf_client = InferenceClient(HUGGINGFACE_TOKEN)
co = cohere.Client(COHERE_KEY)

BASE_PROMPT = """You are an expert career advisor. Improve this resume based on the job description.
Resume: {resume}
Job: {job}
"""

def generate_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"[Gemini failed] {e}")
        return None

def generate_with_huggingface(prompt):
    try:
        response = hf_client.text_generation(prompt, max_new_tokens=300)
        return response
    except Exception as e:
        print(f"[HuggingFace failed] {e}")
        return None

def generate_with_cohere(prompt):
    try:
        response = co.generate(prompt=prompt, max_tokens=300)
        return response.generations[0].text
    except Exception as e:
        print(f"[Cohere failed] {e}")
        return None

def get_suggestions(resume_text, job_text):
    prompt = BASE_PROMPT.format(resume=resume_text, job=job_text)

    print("[INFO] Trying Gemini...")
    response = generate_with_gemini(prompt)
    if response:
        return response.strip()

    print("[INFO] Trying HuggingFace...")
    response = generate_with_huggingface(prompt)
    if response:
        return response.strip()

    print("[INFO] Trying Cohere...")
    response = generate_with_cohere(prompt)
    if response:
        return response.strip()

    return "❌ Sorry, all models failed to generate suggestions at this time."
