import re


def clean_resume_text(text: str) -> str:
    # Remove multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive newlines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Strip leading/trailing spaces
    text = text.strip()

    return text