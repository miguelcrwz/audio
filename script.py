import PyPDF2

with open('file.pdf', 'rb') as path:
    pdfReader = PyPDF2.PdfReader(path)

    for page_num in range(len(pdfReader.pages)):
        page = pdfReader.pages[page_num]
        text = page.extract_text()
