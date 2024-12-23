# https://github.com/microsoft/markitdown

# pip install markitdown
# pip install openai

# Microsoft open-sourced MarkItDown, a Python library that lets you convert any document to Markdown. Huge for LLMs.
 
# It supports:
# • PDF
# • PowerPoint
# • Word
# • Excel
# • Images (EXIF metadata and OCR)
# • Audio (EXIF metadata and speech transcription)
# • HTML
# • Text-based formats (CSV, JSON, XML)
# • ZIP files (iterates over contents) 

from markitdown import MarkItDown
from openai import OpenAI

def convert_pdf_to_markdown(file_path):
    md = MarkItDown()
    result = md.convert(file_path)
    print(result.text_content)

def convert_pdf_with_llm(file_path):
    client = OpenAI()
    md = MarkItDown(llm_client=client, llm_model="gpt-4o")
    result = md.convert(file_path)
    print(result.text_content)

# Example usage

file_path = "Python/invoicesample.pdf"

# convert_pdf_to_markdown(file_path)
convert_pdf_with_llm(file_path)
