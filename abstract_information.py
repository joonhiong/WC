import PyPDF2
import re
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials

for pdf_file in pdf_files:
    file_id = pdf_file['id']
    file = service.files().get_media(fileId=file_id).execute()
    text = extract_text(file)
    information = abstract_information(text)
    print(information)
    
# Function to extract the text from a PDF file
def extract_text(pdf_file):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for i in range(pdf_reader.numPages):
        text += pdf_reader.getPage(i).extractText()
    return text

# Function to abstract information after the keywords
def abstract_information(text):
    information = {}
    lines = text.split("\n")
    for line in lines:
        if "Person(s):" in line:
            person = line.split(":")[1].strip()
            information["Person(s)"] = person
        elif "Email:" in line:
            email = line.split(":")[1].strip()
            information["Email"] = email
        elif "Date:" in line:
            date = line.split(":")[1].strip()
            information["Date"] = date
        elif "Begin:" in line:
            begin = line.split(":")[1].strip()
            information["Begin"] = begin
        elif "End:" in line:
            end = line.split(":")[1].strip()
            information["End"] = end
    return information

# Replace this with your own service account credentials
credentials = Credentials.from_service_account_file(
    'C:\Users\Joon-Vincent\Desktop\WC/wc-test-376310-2632d3768591.json',
    scopes=['https://www.googleapis.com/auth/drive']
)

# Build the Google Drive API client
service = build('drive', 'v3', credentials=credentials)

# Replace this with the ID of your Google Document folder
folder_id = '1cvUlymx1F90RlKtNyDtPQjWsMBoMCEZ6'

# Query the Google Drive API to get a list of all PDF files in the folder
query = "mimeType='application/pdf' and trashed = false and parents in '" + folder_id + "'"
results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
pdf_files = results.get("files", [])

# Loop through the list of PDF files
for pdf_file in pdf_files:
    text = extract_text(pdf_file)
    information = abstract_information(text)
    print(information)
