import os
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup

def pdf_to_html(pdf_path, html_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Extract text from PDF
    text = extract_text(pdf_path)

    # Generate HTML
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

    # Embed images in HTML
    for idx, image in enumerate(images):
        image_path = f"image_{idx}.jpg"
        image.save(image_path, 'JPEG')
        html_content += f"<img src='{image_path}' alt='Page {idx+1} Image'>"

    html_content += """
    </body>
    </html>
    """

    # Write HTML content to file
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"HTML file saved at: {os.path.abspath(html_path)}")

# Path to the PDF file
pdf_path = 'C:\Users\DELL\Desktop\Flask Project\SFAS-13051286_20240206_110141.pdf'

# Path to save the HTML file
html_path = 'newmutualforamt.html'

# Convert PDF to HTML
pdf_to_html(pdf_path, html_path)
