# Replace this with the ID of your Google Document folder
folder_id = '1cvUlymx1F90RlKtNyDtPQjWsMBoMCEZ6'

# Query the Google Drive API to get a list of all PDF files in the folder
query = "mimeType='application/pdf' and trashed = false and parents in '" + folder_id + "'"
results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
pdf_files = results.get("files", [])

# Loop through the list of PDF files
for pdf_file in pdf_files:
    # Get the PDF file content from Google Drive
    file_id = pdf_file['id']
    request = service.files().get_media(fileId=file_id)
    file_content = request.execute()

    # Pass the content of the PDF file to PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(file_content))

    # Extract the text from the PDF file
    text = ""
    for i in range(pdf_reader.numPages):
        text += pdf_reader.getPage(i).extractText()

    # Abstract information from the extracted text
    information = abstract_information(text)
    print(information)
