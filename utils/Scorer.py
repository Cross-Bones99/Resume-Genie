skill_keywords = {
    "python": ["python"],
    "java": ["java"],
    "javascript": ["javascript", "js"],
    "react": ["react", "reactjs", "react.js"],
    "sql": ["sql", "mysql", "postgresql"],
    "machine learning": [
        "machine learning",
        "ml"
    ],
    "deep learning": [
        "deep learning"
    ],
    "artificial intelligence": [
        "artificial intelligence",
        "ai"
    ],
    "generative ai": [
        "generative ai",
        "llm",
        "large language model"
    ],
    "html": ["html"],
    "css": ["css"],
    "node.js": [
        "node.js",
        "nodejs"
    ],
    "flask": ["flask"],
    "streamlit": ["streamlit"],
    "langchain": ["langchain"],
    "git": ["git"],
    "github": ["github"]
}


def calculate_score(resume_text):

    score = 0

    resume_text = resume_text.lower()

    for skill, keywords in skill_keywords.items():

        for keyword in keywords:

            if keyword in resume_text:

                score += 5
                break

    if score > 100:
        score = 100

    return score


def get_missing_skills(resume_text):

    missing_skills = []

    resume_text = resume_text.lower()

    for skill, keywords in skill_keywords.items():

        found = False

        for keyword in keywords:

            if keyword in resume_text:

                found = True
                break

        if not found:

            missing_skills.append(skill)

    return missing_skills