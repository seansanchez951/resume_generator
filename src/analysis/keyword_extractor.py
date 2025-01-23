import re

def extract_keywords(text):
    # Filter meaningful keywords
    keywords = set()
    for word in text.split():
        if word.isalpha() and word.lower() not in {"proficient", "in", "and"}:  # Exclude common words
            keywords.add(word)
    return keywords

