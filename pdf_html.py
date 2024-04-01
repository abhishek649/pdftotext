from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import BytesIO

def pdf_to_html(pdf_path, html_path):
    # Set parameters for text extraction
    laparams = LAParams()

    # Open PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create BytesIO object to hold HTML content
        html_stream = BytesIO()

        # Extract text and write to BytesIO object as HTML
        extract_text_to_fp(pdf_file, html_stream, laparams=laparams, output_type='html')

        # Get HTML content from BytesIO object
        html_content = html_stream.getvalue().decode()
        print(html_content)

        # Write HTML content to file
        with open(html_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

    print(f"HTML file saved at: {html_path}")

# Path to the PDF file
pdf_path = 'SFAS-13051286_20240206_110141.pdf'

# Path to save the HTML file
html_path = 'mutualformat.html'

# Convert PDF to HTML
pdf_to_html(pdf_path, html_path)
