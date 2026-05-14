from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_cover_letter(
    resume_text,
    job_description,
    company_name
):

    prompt = f"""

    Generate a professional cover letter.

    Candidate Resume:
    {resume_text}

    Job Description:
    {job_description}

    Company Name:
    {company_name}

    The cover letter should:
    - sound professional
    - highlight relevant skills
    - be concise
    - be ATS-friendly

    """

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7

    )

    return response.choices[0].message.content