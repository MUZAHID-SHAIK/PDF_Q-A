from sqlalchemy.orm import Session
from .models import Document

def create_document(db: Session, filename: str, text: str) -> Document:
    # Check if the document with the same filename already exists
    existing = db.query(Document).filter(Document.filename == filename).first()
    if existing:
        return existing  # Avoid duplicate insert by returning existing record

    doc = Document(filename=filename, text=text)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def get_document(db: Session, document_id: int) -> Document:
    return db.query(Document).filter(Document.id == document_id).first()