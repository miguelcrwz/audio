import PyPDF2

with open('file.pdf', 'rb') as path:
    pdfReader = PyPDF2.PdfReader(path)
