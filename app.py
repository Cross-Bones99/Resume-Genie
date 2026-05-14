import streamlit as st

from utils.parser import extract_text_from_pdf
from utils.Scorer import calculate_score, get_missing_skills
from utils.matcher import calculate_job_match
from utils.ai_feedback import generate_resume_feedback
from utils.cover_letter import generate_cover_letter
from utils.pdf_generator import create_cover_letter_pdf


st.set_page_config(
    page_title="Resume Genie",
    layout="wide"
)


#Adding custom css




st.markdown("""

<style>

.main {
    padding-top: 1rem;
}

.stMetric {

    background-color: #1e1e1e;

    padding: 15px;

    border-radius: 12px;

    border: 1px solid #333333;

    text-align: center;
}

.stTabs [data-baseweb="tab-list"] {

    gap: 20px;
}

.stTabs [data-baseweb="tab"] {

    background-color: #262730;

    border-radius: 10px;

    padding: 10px 20px;

    color: white;
}

.stButton > button {

    width: 100%;

    border-radius: 10px;

    height: 3em;

    font-size: 16px;

    font-weight: 600;
}

</style>

""", unsafe_allow_html=True)










# SIDEBAR


st.sidebar.title("Resume Genie")

page = st.sidebar.radio(

    "Navigate",

    [
        "Resume Analyzer",
        "Cover Letter Generator"
    ]
)



# RESUME ANALYZER PAGE


if page == "Resume Analyzer":

    st.title("Resume Genie")
    st.subheader("AI Powered Career Suite")

    uploaded_file = st.file_uploader(
        "Upload Your Resume",
        type=["pdf"]
    )

    if uploaded_file:

        st.success("Resume Uploaded Successfully!")

        extracted_text = extract_text_from_pdf(
            uploaded_file
        )



        tab1, tab2, tab3, tab4 = st.tabs([

            "Resume Analysis",

            "ATS Matching",

            "AI Feedback",

            "Resume Content"

        ])



        with tab1:


        
            # SCORE SECTION
        

            score = calculate_score(extracted_text)

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    label="Resume Score",
                    value=f"{score}/100"
                )
            

            # MISSING SKILLS
            

            missing_skills = get_missing_skills(
                extracted_text
            )


            with col3:

                st.metric(
                    label="Missing Skills",
                    value=len(missing_skills)
                )


            st.subheader(
                "Recommended Skills To Add"
            )

            for skill in missing_skills:

                st.write("❌", skill)

       
        
        



        with tab2:

        # ATS MATCHING

            st.subheader(
                "Job Description Matching"
            )

            job_description = st.text_area(
                "Paste Job Description Here"
            )

            if job_description:

                match_score, required_skills, matched_skills = calculate_job_match(
                            extracted_text,
                            job_description
                            )


                with col2:

                    st.metric(
                        label="ATS Match",
                        value=f"{match_score}%"
                    )

                st.write(
                    f"Job Match Score: {match_score}%"
                )

                st.progress(match_score / 100)

                st.subheader("Required Skills")

                st.write(required_skills)

                st.subheader("Matched Skills")

                st.write(matched_skills)

        
        # AI FEEDBACK
        
        with tab3:
        # AI FEEDBACK
            
            st.subheader("AI Resume Review")

            if st.button("Generate AI Feedback"):

                with st.spinner(
                    "Analyzing Resume..."
                ):

                    feedback = generate_resume_feedback(
                        extracted_text
                    )

                    st.write(feedback)

        

        with tab4:
            # EXTRACTED TEXT
            

            st.subheader("Extracted Resume Text")

            st.text_area(
                "Resume Content",
                extracted_text,
                height=300
            )



# COVER LETTER PAGE


elif page == "Cover Letter Generator":

    st.title("AI Cover Letter Generator")

    st.write(
        "Generate professional AI-powered cover letters."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file:

        extracted_text = extract_text_from_pdf(
            uploaded_file
        )

        company_name = st.text_input(
            "Enter Company Name"
        )

        cover_letter_job_description = st.text_area(
            "Enter Job Description"
        )

        if st.button("Generate Cover Letter"):

            with st.spinner(
                "Generating Cover Letter..."
            ):

                cover_letter = generate_cover_letter(
                    extracted_text,
                    cover_letter_job_description,
                    company_name
                )

                st.write(cover_letter)

                pdf_file = create_cover_letter_pdf(
                    cover_letter
                )

                st.download_button(

                    label="Download Cover Letter PDF",

                    data=pdf_file,

                    file_name="cover_letter.pdf",

                    mime="application/pdf"
                )