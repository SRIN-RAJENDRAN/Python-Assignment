# main.py
from typing import List

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

# Define the database URL (SQLite by default)
DATABASE_URL = "sqlite:///./notedatabase.db"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define a base for declarative models
Base = declarative_base()

# Define the Note model
class Note(Base):
    """SQLAlchemy model for the Note entity. it's creating table"""
    __tablename__= "notes" # it table name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

# Define Pydantic models for API requests and responses
class NoteBase(BaseModel):
    """Base Pydantic model for note attributes."""
    title: str
    content: str

class NoteCreate(NoteBase):
    """Pydantic model for creating a new note."""
    pass

class NoteUpdate(NoteBase):
    """Pydantic model for updating an existing note."""
    pass

class NoteResponse(NoteBase):
    """Pydantic model for the API response of a note."""
    id: int

    class Config:
        from_attributes  = True

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    """Dependency to create and close a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a SessionLocal class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the FastAPI application
api = FastAPI(title="Notes API", description="A simple RESTful API for managing notes.")

# --- CRUD Operations ---
# Creating a Notes
@api.post("/notes/", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    """Creates a new note."""
    db_note = Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@api.get("/notes/", response_model=List[NoteResponse],status_code=302)
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieves a list of notes."""
    notes = db.query(Note).offset(skip).limit(limit).all()
    return notes

@api.get("/notes/{note_id}", response_model=NoteResponse,status_code=302)
def read_note(note_id: int, db: Session = Depends(get_db)):
    """Retrieves a specific note by ID."""
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note is not found,please Check the note id")
    return db_note

@api.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    """Updates an existing note by ID."""
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note is not found,please Check the note id")
    for key, value in note.dict(exclude_unset=True).items():
        setattr(db_note, key, value)
    db.commit()
    db.refresh(db_note)
    return db_note

@api.delete("/notes/{note_id}", response_model=NoteResponse)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    """Deletes a note by ID."""
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(db_note)
    db.commit()
    return db_note
