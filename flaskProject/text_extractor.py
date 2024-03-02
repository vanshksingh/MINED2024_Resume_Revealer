import os
import tempfile

import pytesseract
from docx import Document
from pdf2image import convert_from_bytes
from PIL import Image
import textract
import io
import tkinter as tk
from tkinter import filedialog

def extract_text(file_data):
    file_name, file_content = file_data
    file_extension = os.path.splitext(file_name)[1].lower()

    if file_extension == '.pdf':
        pages = convert_from_bytes(file_content, 300)
        text = ''
        for page in pages:
            text += pytesseract.image_to_string(page)
        return (file_name, text)
    elif file_extension == '.docx':
        doc = Document(io.BytesIO(file_content))
        text = '\n'.join([para.text for para in doc.paragraphs])
        return (file_name, text)
    elif file_extension == '.doc':
        with tempfile.NamedTemporaryFile(suffix='.doc', delete=False) as tmp_file:
            tmp_file.write(file_content)
            tmp_file_path = tmp_file.name
        text = textract.process(tmp_file_path, encoding='utf-8')
        os.unlink(tmp_file_path)  # Remove temporary file
        return (file_name, text.decode('utf-8'))
    elif file_extension == '.txt':
        text = file_content.decode('utf-8')
        return (file_name, text)
    elif file_extension in ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']:
        image = Image.open(io.BytesIO(file_content))
        text = pytesseract.image_to_string(image)
        return (file_name, text)
    elif file_extension == '.html':
        # You can use BeautifulSoup or any other HTML parsing library to extract text from HTML
        text = file_content.decode('utf-8')
        return (file_name, text)
    else:
        return (file_name, "Unsupported file type")

def open_file_window():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    file_paths = filedialog.askopenfilenames()  # Open file window to select multiple files
    files = []
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        with open(file_path, 'rb') as file:
            file_content = file.read()
            files.append((file_name, file_content))
    return files

def process_files(files):
    extracted_texts = []
    for file_data in files:
        extracted_texts.append(extract_text(file_data))
    return extracted_texts

def main():
    files = open_file_window()  # Open file window to select files
    if files:
        extracted_texts = process_files(files)
        for file_name, text in extracted_texts:
            print(f"Extracted text from {file_name}: {text}")
    else:
        print("No files selected.")

