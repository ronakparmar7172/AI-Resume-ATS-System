import re, nltk, PyPDF2, docx2txt
from nltk.corpus import stopwords

nltk.download('stopwords')

def extract_text(file):
    if file.name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        return " ".join(p.extract_text() for p in reader.pages)
    elif file.name.endswith('.docx'):
        return docx2txt.process(file)
    return file.read().decode('utf-8')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z ]', ' ', text)
    return " ".join(w for w in text.split() if w not in stopwords.words('english'))
