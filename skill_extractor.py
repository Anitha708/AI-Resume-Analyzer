import re


SKILLS = {
    "Programming": [
        "python",
        "java",
        "c++",
        "javascript"
    ],

    "AI & Machine Learning": [
        "artificial intelligence",
        "machine learning",
        "machine learning algorithms",
        "generative ai",
        "deep learning",
        "tensorflow",
        "keras",
        "scikit learn"
    ],

    "Data & Analytics": [
        "data analysis",
        "exploratory data analysis",
        "eda",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "power bi",
        "sql"
    ],

    "Web & Deployment": [
        "streamlit",
        "git",
        "github"
    ]
}


def normalize_for_matching(text):

    text = text.lower()

    # Remove spaces between individual characters
    # P y t h o n -> python
    text = re.sub(
        r'(?<!\w)(?:[a-z]\s+){2,}[a-z](?!\w)',
        lambda m: m.group(0).replace(" ", ""),
        text
    )

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    return text


def extract_skills(text):

    text = normalize_for_matching(text)

    found_skills = {}

    for category, skills in SKILLS.items():

        detected = []

        for skill in skills:

            skill_normalized = skill.lower()

            # Normal matching
            pattern = r'(?<![a-z])' + re.escape(skill_normalized) + r'(?![a-z])'

            if re.search(pattern, text):

                detected.append(skill.title())

        if detected:

            found_skills[category] = detected

    return found_skills