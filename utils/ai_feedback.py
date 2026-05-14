from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_resume_feedback(resume_text):

    prompt = f"""

    You are an expert ATS resume reviewer.

    Analyze this resume and provide:

    1. Strengths
    2. Weaknesses
    3. Missing Skills
    4. ATS Improvements
    5. Final Suggestions

    Resume:

    {resume_text}

    """

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5

    )

    return response.choices[0].message.content