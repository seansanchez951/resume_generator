import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.generator.resume_writer import rewrite_resume

def test_rewrite_resume():
    resume_text = "Experienced in Python and SQL."
    job_keywords = {"Python", "Machine Learning"}
    tailored_resume = rewrite_resume(resume_text, job_keywords)
    assert "Python" in tailored_resume
    assert "Machine Learning" in tailored_resume
