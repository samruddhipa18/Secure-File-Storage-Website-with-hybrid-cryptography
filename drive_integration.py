import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# Path to your credentials file
CREDENTIALS_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate and build the Drive API client
def authenticate_drive():
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    return service

# Upload file to Google Drive
def upload_to_drive(file_path, folder_id=None):
    service = authenticate_drive()
    file_metadata = {'name': os.path.basename(file_path)}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(
        body=file_metadata, media_body=media, fields='id').execute()
    print(f"File ID: {file.get('id')}")
    return file.get('id')

# Download file from Google Drive
def download_from_drive(file_id, destination_path):
    service = authenticate_drive()
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination_path, 'wb')
    
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")

    print("Download Complete.")
    return destination_path

# Optional: Create a folder on Google Drive (useful for organizing files by user/project)
def create_drive_folder(folder_name):
    service = authenticate_drive()
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = service.files().create(body=folder_metadata, fields='id').execute()
    print(f"Folder ID: {folder.get('id')}")
    return folder.get('id')
