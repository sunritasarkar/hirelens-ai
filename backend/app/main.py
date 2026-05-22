from fastapi import FastAPI, UploadFile, File
import pdfplumber
import os
from fastapi.middleware.cors import CORSMiddleware

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

    return {
        "filename": file.filename,
        "extracted_text": extracted_text
    }