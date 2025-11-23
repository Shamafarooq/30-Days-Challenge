import streamlit as st
import asyncio
from agent import pdf_summarizer_agent,quiz_generator_agent
from agents import Runner
import os



st.title("PDF Study Notes Summarizer & Quiz Generator")

# A. Upload Section
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("Extracting text from PDF...")
    
    # Run the agent to extract and clean text
    async def extract_and_clean():
        result = await Runner.run(pdf_summarizer_agent , f"Extract text from temp.pdf and clean it.")
        return result.final_output

    cleaned_text = asyncio.run(extract_and_clean())
    
    st.write("Generating summary...")
    
    # Run the agent to summarize the text
    async def summarize():
        result = await Runner.run(pdf_summarizer_agent, f"Summarize the following text:\n{cleaned_text}")
        return result.final_output

    summary = asyncio.run(summarize())
    
    st.subheader("Summary")
    st.markdown(f"""
    <div style="border: 1px solid #e6e6e6; border-radius: 5px; padding: 10px;">
    {summary}
    </div>
    """, unsafe_allow_html=True)

    # B. Quiz Section
    if st.button("Generate Quiz"):
        st.write("Generating quiz...")
        
        # Run the agent to generate a quiz
        async def generate_quiz():
            result = await Runner.run(quiz_generator_agent, f"Generate a quiz from the following text and make sure give the multiple choies questions:\n{cleaned_text}")
            return result.final_output

        quiz = asyncio.run(generate_quiz())

        st.subheader("Quiz")
        st.write(quiz)

    # Clean up the temporary file
    os.remove("temp.pdf")
