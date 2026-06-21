# core/ingestion.py
import pypdf

def extract_text_from_pdf(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text: 
            full_text += text + "\n"
    return full_text

def split_text_into_chunks(text, chunk_size=500, overlap=100):
    """Advanced Sliding Window Chunking for Better Context Retention"""
    words = text.split()
    chunks = []
    
    i = 0
    while i < len(words):
        chunk_words = words[i:i + chunk_size]
        chunks.append(" ".join(chunk_words))
        i += (chunk_size - overlap)  # Sliding window overlap logic
        
    return chunks