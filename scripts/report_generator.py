import os
from jinja2 import Template
from weasyprint import HTML

def generate_pdf(data, output_filename="ats_report_user1.pdf"):
    template_path = os.path.join("templates", "ats_report_template.html")
    output_path = os.path.join("outputs", output_filename)

    # Read HTML template
    with open(template_path, "r", encoding="utf-8") as f:
        template = Template(f.read())

    # Render HTML with data
    html_out = template.render(data)

    # Generate PDF
    HTML(string=html_out).write_pdf(output_path)

    return output_path
