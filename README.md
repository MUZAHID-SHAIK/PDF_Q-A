# PDF Q\&A App (FastAPI + React + Ollama + LangChain)

This is a full-stack application that allows users to **upload PDF documents** and **ask questions** based on their content. The application processes PDFs using local AI models via **Ollama**, and uses **LangChain** for QA chain building.

---

## ✨ Features

* Upload PDF documents
* Extract and store content
* Ask questions about any uploaded PDF
* View accurate answers powered by LLMs
* Simple, clean frontend using React

---

## 🧱 Technologies Used

### Backend

* [FastAPI](https://fastapi.tiangolo.com/): For API creation
* [LangChain](https://www.langchain.com/): To handle embedding + LLM logic
* [Ollama](https://ollama.com): To run models like `llama3`, `mistral`, `tinyllama` locally
* [SQLite](https://www.sqlite.org/index.html): Lightweight DB to store PDF metadata
* [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/): To extract text from PDFs

### Frontend

* React.js (Hooks, Functional Components)
* Axios for API calls
* CSS (clean layout)

---

## 📁 Folder Structure

```
pdf_qa_app/
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI entry point
│   │   ├── crud.py            # DB access functions
│   │   ├── llm_utils.py       # LangChain + Ollama logic
│   │   ├── pdf_utils.py       # PDF text extraction
│   │   ├── models.py          # SQLAlchemy models
│   │   ├── schemas.py         # Pydantic models
│   │   └── database.py        # DB setup
│   └── uploaded_files/        # Uploaded PDF files
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── Upload.js
│   │   ├── QA.js
│   │   ├── api.js
│   │   └── styles.css
└── README.md
```

---

## 🚀 Getting Started

### 1. Prerequisites

* Python 3.10+
* Node.js + npm
* [Ollama installed](https://ollama.com/download)

### 2. Backend Setup

```bash
cd pdf_qa_app/backend
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt

# Start FastAPI server
uvicorn app.main:app --reload
```

### 3. Frontend Setup

```bash
cd pdf_qa_app/frontend
npm install
npm start
```

---

## ⚙️ Ollama Setup

Install and run a lightweight model (example: `tinyllama`):

```bash
ollama run tinyllama
```

If you're using `llama3` or `mistral`, ensure your system has at least 8GB+ free RAM.

You can switch models by editing `llm_utils.py`:

```python
llm = OllamaLLM(model="tinyllama")
```

---

## 📂 API Endpoints

### `POST /upload`

* Accepts: PDF file
* Returns: `{"id": 1, "filename": "yourfile.pdf"}`

### `POST /ask`

* Body: `{ "document_id": 1, "question": "What is this document about?" }`
* Returns: `{ "answer": "..." }`

---

## 📅 Example Workflow

1. Go to [http://localhost:3000](http://localhost:3000)
2. Upload a PDF (e.g. resume, report, syllabus)
3. Copy the document ID returned after upload
4. Enter your question and document ID
5. View answer on screen

---

## ✅ Tips

* Use small PDF files for better performance
* Try `tinyllama` if running into memory errors
* Check console/logs if answer is empty or slow

---

## 🚨 Troubleshooting

### ❌ Upload works, but ask gives empty/incorrect answer?

* Make sure document\_id matches what was returned after upload
* Confirm that Ollama model is running and not crashing

### ❌ `Model requires more memory`?

* Try lighter model: `tinyllama`
* Free up system memory (close browser tabs, apps)

---

##  Credits

Built as part of Fullstack Internship Assignment 2025.

---

