import PyPDF2

def extract_text(pdf_file):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for i in range(pdf_reader.numPages):
        text += pdf_reader.getPage(i).extractText()
    return text
