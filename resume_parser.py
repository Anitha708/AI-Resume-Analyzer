from pypdf import PdfReader
from docx import Document


def extract_pdf_text(file):
    """Extract text from a PDF resume."""
    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx_text(file):
    """Extract text from a DOCX resume."""
    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text


def extract_resume_text(file):
    """Extract text based on the uploaded file type."""

    file_name = file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_pdf_text(file)

    elif file_name.endswith(".docx"):
        return extract_docx_text(file)

    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")