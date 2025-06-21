from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, pdf_utils, llm_utils
from .database import engine, Base, get_db
import os
import traceback

# Initialize DB schema
Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI()

# ✅ Enable CORS for frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory to save uploaded PDFs
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload", response_model=schemas.UploadResponse)
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

        # Save PDF to disk
        path = os.path.join(UPLOAD_DIR, file.filename)
        contents = await file.read()
        with open(path, "wb") as f:
            f.write(contents)

        # Extract text from PDF
        text = pdf_utils.extract_text_from_pdf(path)

        # Save document in database
        doc = crud.create_document(db, filename=file.filename, text=text)

        return {"id": doc.id, "filename": doc.filename}

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


@app.post("/ask", response_model=schemas.QAResponse)
def ask_question(req: schemas.QARequest, db: Session = Depends(get_db)):
    try:
        # Retrieve document from DB
        doc = crud.get_document(db, req.document_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found.")

        # Ask question using the document text
        answer = llm_utils.answer_question(doc.text, req.question)

        return {"answer": answer}

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Answer generation failed: {str(e)}")
