import sys
import os
from docx import Document
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.parsers.resume_parser import parse_docx, parse_pdf, parse_resume


def test_parse_docx():
    file_path = "data/resumes/sample_resume.docx"
    assert os.path.exists(file_path)
    text = parse_docx(file_path)
    assert "Sample resume text." in text

def test_parse_pdf():
    file_path = "data/resumes/sample_resume.pdf"
    assert os.path.exists(file_path)
    text = parse_pdf(file_path)
    assert "Sample resume text." in text


def test_parse_resume_invalid_file():
    with patch("os.path.exists", return_value=False):
        file_path = "data/resumes/unsupported_file.txt"
        try:
            parse_resume(file_path)
        except FileNotFoundError as e:
            assert str(e) == f"File not found: {file_path}"
