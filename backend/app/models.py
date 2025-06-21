from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)  # removed unique=True to avoid IntegrityError
    upload_date = Column(DateTime, default=datetime.utcnow)
    text = Column(String)
