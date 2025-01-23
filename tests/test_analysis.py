import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Debugging: Print sys.path
print("sys.path:", sys.path)

from src.analysis.keyword_extractor import extract_keywords


def test_extract_keywords():
    text = "Proficient in Python, SQL, and Machine Learning."
    keywords = extract_keywords(text)
    assert "Python" in keywords
    assert "SQL" in keywords
    assert "Machine" in keywords
    assert len(keywords) == 3  # Ensure the count matches expectations
