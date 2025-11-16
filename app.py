import streamlit as st
from langchain_groq import ChatGroq
import pypdf as PyPDF2
import os
from dotenv import load_dotenv
from utils import chunk_text

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("Set GROQ_API_KEY in .env or environment variables")

# Use a supported model
MODEL_NAME = "llama-3.1-8b-instant"

client = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME,
    temperature=0.2,
    max_tokens=300,
)

st.title("Project- 23 PDF Summarizer with Groq and Streamlit")

uploaded = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded:
    reader = PyPDF2.PdfReader(uploaded)
    raw_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            raw_text += page_text + " "

    st.subheader("Extracted Text")
    st.text_area("PDF Raw Text", raw_text[:2000] + "...", height=150)

    st.subheader("Processing…")
    chunks = chunk_text(raw_text, max_tokens=700)
    st.write(f"Chunks created: {len(chunks)}")

    summaries = []

    for idx, chunk in enumerate(chunks):
        with st.spinner(f"Summarizing chunk {idx+1}/{len(chunks)}…"):
            result = client.invoke(
                f"Summarize this text clearly and concisely:\n\n{chunk}"
            )
            summaries.append(result.content)

    final_summary = "\n".join(summaries)

    st.subheader("Final Summary")
    st.write(final_summary)
