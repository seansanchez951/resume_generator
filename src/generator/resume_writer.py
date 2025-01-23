def rewrite_resume(resume_text, job_keywords):
    tailored_resume = resume_text
    for keyword in job_keywords:
        if keyword not in resume_text:
            tailored_resume += f" {keyword}"
    return tailored_resume
