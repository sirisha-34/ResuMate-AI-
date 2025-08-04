import re

def check_formatting_issues(resume_text):
    issues = []
    if not re.search(r"\d{10}", resume_text):
        issues.append("Phone number missing")
    if "@" not in resume_text:
        issues.append("Email missing")
    return issues