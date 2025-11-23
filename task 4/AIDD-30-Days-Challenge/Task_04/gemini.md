Role: Senior Python AI Engineer

Objective: Build a "PDF Study Notes Summarizer & Quiz Generator Agent" using Streamlit and the openai-agents SDK, powered by Gemini CLI + Context7 MCP.

1. Project Overview

The goal is to develop a smart agent that:

Reads a PDF.

Generates a clean, structured summary.

Creates a quiz (MCQs or mixed format) based on the PDF content.

UI: Streamlit (recommended
Model: Gemini model via OpenAI Agents SDK
Tools: PyPDF for extraction, openai-agents for reasoning, Context7 MCP for docs & tool access.

2. Critical Technical Constraints
1. Zero-Bloat Protocol (Mandatory)

Do NOT add unnecessary functions.

Follow strictly the patterns shown in the SDK documentation.

No hallucinated features — use ONLY what exists in docs.

2. API Configuration

SDK: openai-agents (NOT the normal openai library)

Base URL:
https://generativelanguage.googleapis.com/v1beta/openai/

API Key: Use GEMINI_API_KEY from .env.

Model: Use OpenaiChatCompletionModel with the correct Gemini model.

3. SDK-Specific Requirements

You MUST use:

correct tool format (decorator or FunctionTool depending on docs)

correct Agent initialization

correct model binding

If confused → recheck docs using get-library-docs.

4. Error Recovery Protocol

If you get:

SyntaxError

AttributeError

ImportError

→ STOP.
→ Do not guess.
→ Re-run get-library-docs.
→ Rewrite code only after confirming syntax.

5. Dependency Management

Use uv for installation.
Install ONLY the required packages:

streamlit

pypdf

openai-agents

python-dotenv

3. Architecture & File Structure
.
├── .env                     # API Key
├── extract.py              # PDF extraction tools
├── agent.py                # Agent + model + tools binding
├── app.py                  # Streamlit UI logic
├── prompt_screenshot.png   # Screenshot of Gemini CLI prompt
└── pyproject.toml          # uv dependencies

4. Implementation Steps

(Exactly follow this order)

Step 1: SDK Documentation Verification

Before writing ANY code:

Run MCP tool:
get-library-docs for openai-agents

Study:

tool registration rules

agent initialization

model usage patterns

correct async call format

If unsure → call again.

Step 2: PDF Tools (extract.py)

Implement ONLY two functions:

extract_text_from_pdf(file_path: str)
– Use PyPDF, return raw extracted text.

clean_text(text: str)
– Remove newlines, extra spaces.

These functions must be wrapped as SDK tools using the correct tool wrapper found in docs.

Step 3: Agent Configuration (agent.py)

Initialize Gemini model using base URL.

Use correct OpenaiChatCompletionModel.

Import & register tools from extract.py.

Add system prompt:

"Summarize uploaded PDFs and generate quizzes based only on extracted text. Produce clean and structured output."

No extra behavior allowed.

Step 4: Streamlit UI (app.py)

Implement the following:

A) Upload Section

User uploads PDF

Call the extraction tool → get text

Call the agent → summary

Show summary inside a beautiful Streamlit card/block

B) Quiz Section

Button: Generate Quiz

Agent uses original PDF text to create MCQs or mixed-style questions

Display quiz neatly

❗ No need for multi-page Streamlit app
❗ No streaming
❗ No complicated state management

Step 5: Environment Setup

Create .env with GEMINI_API_KEY=xxxxxxxx

Add dependencies to pyproject.toml

Use uv to install

5. Testing Scenarios
1. Summarization Check

Upload a PDF → Agent should return a structured summary.

2. Quiz Generation Check

After summary, click Generate Quiz → Agent produces MCQs.

3. Failure Handling

Upload corrupted PDF → Tool returns empty string or safe error.

4. Correct Tool Invocation

Terminal should show:

[tool call: extract_text_from_pdf]

6. CLI Requirement

You MUST include a screenshot of the Gemini CLI prompt you used to bootstrap the agent:

Example prompt:

Build a PDF Summarizer + Quiz Generator agent using openai-agents SDK.
Tools: extract_text_from_pdf, clean_text.
UI: Streamlit.


Save it as:

prompt_screenshot.png
inside the project folder.