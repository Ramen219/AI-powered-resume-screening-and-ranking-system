import re  # Import the re module for regular expressions
import PyPDF2  # Import the PyPDF2 library for working with PDF files
import docx2txt  # Import the docx2txt library for extracting text from DOCX files

def extract_text(file):
    # Define a function to extract text from a file, which can be either a PDF or DOCX
    if file.filename.endswith('.pdf'):
        # Check if the file is a PDF
        pdf_reader = PyPDF2.PdfReader(file)
        # Create a PdfReader object to read the PDF file
        text = ''.join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        # Extract text from each page of the PDF and join them into a single string

    elif file.filename.endswith('.docx'):
        # Check if the file is a DOCX
        text = docx2txt.process(file)
        # Use docx2txt to extract text from the DOCX file

    else:
        # If the file is neither a PDF nor a DOCX
        text = ''
        # Set the text to an empty string

    return text
    # Return the extracted text
