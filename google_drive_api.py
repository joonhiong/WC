from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials

def get_pdf_files(credentials, folder_id):
    # Build the Google Drive API client
    service = build('drive', 'v3', credentials=credentials)

    # Query the Google Drive API to get a list of all PDF files in the folder
    query = "mimeType='application/pdf' and trashed = false and parents in '" + folder_id + "'"
    results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
    pdf_files = results.get("files", [])
    return pdf_files

def move_pdf_to_folder(credentials, file_id, folder_id):
    # Build the Google Drive API client
    service = build('drive', 'v3', credentials=credentials)

    # Update the parent folder of the file
    file = service.files().update(fileId=file_id, addParents=folder_id).execute()
    return file
