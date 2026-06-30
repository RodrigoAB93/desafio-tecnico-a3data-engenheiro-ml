import re

def clean_text(text: str) -> str:
    """Removes excess whitespace and normalizes newlines."""
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()