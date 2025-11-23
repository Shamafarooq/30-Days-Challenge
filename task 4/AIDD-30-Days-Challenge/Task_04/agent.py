import os
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from extract import extract_text_from_pdf, clean_text
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize the model
provider = AsyncOpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

# 2. Define the system prompt
pdf_system_prompt = "Your job is to read the extracted text from a PDF and generate a clear, concise, and meaningful summary. Focus only on the important points. Do not add extra details or assumptions. Keep the summary easy to understand and well-structured."
quiz_system_prompt = "Your task is to read the original PDF text and generate a quiz based strictly on that content. Create clear, accurate questions without adding outside information. Support MCQs or mixed-style quizzes (MCQs, short answers, true/false). Keep questions relevant, unambiguous, and aligned with the PDF material."

# 3. Create the agent
pdf_summarizer_agent = Agent(
    name="PDF Summarizer",
    instructions=pdf_system_prompt,
    model=model,
    tools=[extract_text_from_pdf, clean_text],
)
quiz_generator_agent = Agent(
    name="Quiz Generator",
    instructions=quiz_system_prompt,
    model=model,
)

