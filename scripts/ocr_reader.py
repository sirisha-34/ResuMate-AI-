import pytesseract
from PIL import Image

def extract_text_from_image(img_bytes):
    img = Image.open(img_bytes)
    return pytesseract.image_to_string(img)