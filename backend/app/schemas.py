from pydantic import BaseModel
from datetime import datetime

class DocumentSchema(BaseModel):
    id: int
    filename: str
    upload_date: datetime

    class Config:
        from_attributes = True  # Updated for Pydantic v2

class UploadResponse(BaseModel):
    id: int
    filename: str

class QARequest(BaseModel):
    document_id: int
    question: str

class QAResponse(BaseModel):
    answer: str
