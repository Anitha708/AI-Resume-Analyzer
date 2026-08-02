import re


def clean_text(text):
    # Normalize line breaks
    text = text.replace("\n", " ")

    # Fix character-spaced words
    # Example:
    # "P y t h o n" -> "Python"
    # "M a c h i n e  L e a r n i n g" -> "Machine Learning"

    pattern = r'\b(?:[A-Za-z]\s+){2,}[A-Za-z]\b'

    def join_characters(match):
        return match.group(0).replace(" ", "")

    text = re.sub(pattern, join_characters, text)

    # Normalize multiple spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()