import extract_pdf_text
import abstract_information
import google_drive_api
from google.oauth2.service_account import Credentials

# Replace this with your own service account credentials
credentials = Credentials.from_service_account_file(
    'C:\Users\Joon-Vincent\Desktop\WC/wc-test-376310-2632d3768591.json',
    scopes=['https://www.googleapis.com/auth/drive']
)

# Replace this with the ID of your Google Document folder
folder_id = '1cvUlymx1F90RlKtNyDtPQjWsMBoMCEZ6'

pdf_files = google_drive_api.get_pdf_files(credentials, folder_id)

# Loop through the list of PDF files
for pdf_file in pdf_files:
    try:
        text = extract_pdf_text.extract_text(pdf_file)
    except Exception as e:
        print("Error in extracting text from PDF file:", e)
        continue
    try:
        information = abstract_information.abstract_information(text)
        print(information)
    except Exception as e:
        print("Error in abstracting information from extracted text:", e)
        continue