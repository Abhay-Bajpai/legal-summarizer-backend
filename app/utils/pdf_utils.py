import pdfplumber

def extract_text_from_pdf(file_path):
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ''
            text.append(page_text)
    return '\n'.join(text)
