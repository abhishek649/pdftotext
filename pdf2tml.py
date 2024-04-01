import os
import io
import fitz  # PyMuPDF
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup

def extract_images_and_text(pdf_path):
    images = []
    text = extract_text(pdf_path)
    
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = io.BytesIO(image_bytes)
            images.append(image)
    
    return text, images

def generate_html(text, images, html_path):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>PDF to HTML</title>
    </head>
    <body>
        <div>
            {text}
        </div>
    """
    
    for idx, image in enumerate(images):
        image_path = f"image_{idx}.jpg"
        with open(image_path, "wb") as img_file:
            img_file.write(image.getvalue())
        html_content += f"<img src='{image_path}' alt='Image {idx+1}'>"

    html_content += """
    </body>
    </html>
    """

    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"HTML file saved at: {os.path.abspath(html_path)}")

# Path to the PDF file
pdf_path = 'SFAS-13051286_20240206_110141.pdf'

# Path to save the HTML file
html_path = 'mostrecentmutual.html'

# Extract text and images from PDF
text, images = extract_images_and_text(pdf_path)

# Generate HTML
generate_html(text, images, html_path)
