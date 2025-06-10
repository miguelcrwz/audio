import PyPDF2
import pyttsx3

speak = pyttsx3.init()

with open('file.pdf', 'rb') as path:
    pdfReader = PyPDF2.PdfReader(path)

    for page_num in range(len(pdfReader.pages)):
        page = pdfReader.pages[page_num]
        text = page.extract_text()

        if text:
            print(f"\nREADING PAGE {page_num + 1}:\n")
            print(text)
            speak.say(text)
            speak.runAndWait()

speak.stop()
