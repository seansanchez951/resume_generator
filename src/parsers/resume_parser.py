import os
import re
from docx import Document
from PyPDF2 import PdfReader

def parse_docx(file_path):
    """
    Extracts text from a DOCX file.
    """
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)

def parse_pdf(file_path):
    """
    Extracts text from a PDF file.
    """
    try:
        # Open the PDF file in read-binary mode
        with open(file_path, 'rb') as file:
            # Initialize a PDF reader object
            reader = PdfReader(file)
            
            # Initialize an empty string to hold the extracted text
            extracted_text = ""
            
            # Loop through each page and extract text
            for page in reader.pages:
                extracted_text += page.extract_text()
                
            return extracted_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def parse_resume(file_path):
    """
    Extracts text from a resume (PDF or DOCX).
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == ".docx":
        return parse_docx(file_path)
    elif file_extension == ".pdf":
        return parse_pdf(file_path)
    else:
        raise ValueError("Unsupported file format. Please use a DOCX or PDF file.")
    









