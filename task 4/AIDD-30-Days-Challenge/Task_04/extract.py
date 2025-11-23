from agents import function_tool
from PyPDF2 import PdfReader

@function_tool
def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        file_path: The path to the PDF file.

    Returns:
        The extracted text.
    """
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

@function_tool
def clean_text(text: str) -> str:
    """
    Cleans the extracted text by removing newlines and extra spaces.

    Args:
        text: The text to clean.

    Returns:
        The cleaned text.
    """
    hekj = " ".join(text.split())
    print("===="*50)
    print(hekj)
    return " ".join(text.split())
