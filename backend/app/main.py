from fastapi import FastAPI, UploadFile, File
import pdfplumber
import os
from fastapi.middleware.cors import CORSMiddleware
from app.utils.text_cleaner import clean_resume_text
from app.utils.section_parser import extract_sections

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "HireLens AI Backend Running Successfully"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    
    # Create uploads folder if not exists
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = ""

    # Extract text from PDF
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
    
    cleaned_text = clean_resume_text(extracted_text)
    sections = extract_sections(cleaned_text)
    return {
    "filename": file.filename,
    "extracted_text": cleaned_text,
    "sections": sections
}