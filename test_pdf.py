import pdfplumber

pdf_path = r"C:\Users\ANITHA DEVI\Downloads\Resume(23mh1a0489).pdf"

with pdfplumber.open(pdf_path) as pdf:
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

print(text[:3000])