skill_keywords = {
    "python": ["python"],
    "java": ["java"],
    "javascript": ["javascript", "js"],
    "react": ["react", "reactjs"],
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
    "flask": ["flask"],
    "streamlit": ["streamlit"],
    "langchain": ["langchain"],
    "git": ["git"],



    "django": ["django"],

    "fastapi": ["fastapi"],

    "nodejs": ["nodejs", "node.js"],

    "mongodb": ["mongodb"],

    "docker": ["docker"],

    "kubernetes": ["kubernetes", "k8s"],

    "tensorflow": ["tensorflow"],

    "pytorch": ["pytorch"],

    "nlp": [
        "nlp",
        "natural language processing"
    ],

    "aws": ["aws", "amazon web services"],

    "html": ["html"],

    "css": ["css"],

    "bootstrap": ["bootstrap"],

    "tailwind": ["tailwind", "tailwind css"],
}


def calculate_job_match(resume_text,job_description):

    resume_text = resume_text.lower()

    job_description = job_description.lower()

    required_skills = []

    matched_skills = []

    for skill, keywords in skill_keywords.items():

        skill_present_in_jd = False

        skill_present_in_resume = False

        for keyword in keywords:

            if keyword in job_description:
                skill_present_in_jd = True

            if keyword in resume_text:
                skill_present_in_resume = True

        if skill_present_in_jd:

            required_skills.append(skill)

            if skill_present_in_resume:
                matched_skills.append(skill)

    if len(required_skills) == 0:

        return 0, [], []

    match_percentage = (
        len(matched_skills)
        / len(required_skills)
    ) * 100

    return (
        round(match_percentage, 2),
        required_skills,
        matched_skills
    )