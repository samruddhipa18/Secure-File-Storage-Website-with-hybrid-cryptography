Project Overview: Secure File Storage Website with Hybrid Cryptography
This website offers a platform to securely upload, store, and retrieve files using a hybrid cryptography approach. Here’s a detailed explanation of the methodology, followed by the steps for running and using the site.

Methodology
The project is broken into two primary stages: File Storage and File Retrieval. Here's a step-by-step look at how each stage works.

1. File Storage (Encryption and Upload)
Step 1: File Upload by User

The user begins by uploading a file to the website, which will be securely stored in encrypted form.
Step 2: File Partitioning

Once uploaded, the file is split into N parts. Partitioning the file into smaller segments enhances security by reducing the exposure of sensitive data if any single part is accessed.
Step 3: Encryption with Multiple Algorithms

Each part is then encrypted using different algorithms in a round-robin sequence (e.g., AES for Part 1, DES for Part 2, RSA for Part 3, and so on). This diversity in encryption algorithms further secures the file against unauthorized decryption.
The encryption keys for each algorithm are stored in a secure manner, but only the user has access to the "master key" needed to decrypt these individual encryption keys.
Step 4: Securing Encryption Keys

The encryption keys used for each file part are encrypted with another algorithm. The user receives this "master key" as a public key, which will be necessary later for decryption.
Step 5: Storage on Google Drive via API

Each encrypted part of the file is uploaded to the user’s Google Drive account using the Google Drive API.
To organize the encrypted parts, each file upload could create a dedicated folder on Google Drive, ensuring that all parts of one file are stored together.
Step 6: Metadata Storage

A metadata file is created, storing essential information about the encryption sequence and algorithms used for each file part. This metadata is also encrypted and stored on Google Drive, ensuring it remains secure.
2. File Retrieval (Decryption and Download)
Step 1: Upload the Master Key

When a user wants to retrieve their file, they upload their master key to the website. This key is used to decrypt the individual encryption keys for each file part.
Step 2: Downloading Encrypted Parts from Google Drive

The website fetches each encrypted part from the user’s Google Drive using file IDs or folder references stored in the metadata file.
Step 3: Decrypting Each Part

Each downloaded part is decrypted with its corresponding algorithm, using the decryption keys obtained from the master key.
Step 4: Reassembling the Original File

After decrypting all parts, the website reassembles them into the original file, which is then made available for download by the user.
How to Run the Website
To set up and run the website locally or on a server, follow these steps:

Prerequisites
Python 2.7.15 (for compatibility with some libraries)
Google Cloud Credentials for accessing Google Drive API
Required Packages: Listed in requirements.txt
Setup and Execution
Install Dependencies

Run pip install -r requirements.txt to install all necessary packages, including cryptography and Google Drive API libraries.
Google Drive API Configuration

In your Google Cloud Console, enable the Google Drive API and download the credentials file (credentials.json).
Place credentials.json in the project directory to allow the website to authenticate with Google Drive on behalf of the user.
Run the Web Application

Execute the command python app.py to start the server.
Open a browser and navigate to http://localhost:5000 (or the assigned port) to access the website.
Using the Website

File Upload: Go to the file upload page, choose your file, and upload it. The website will handle encryption, partitioning, and storage on Google Drive.
Download and Decryption: When you want to retrieve your file, upload the master key. The site will decrypt and reassemble the file for download.
Error Handling and Troubleshooting

If you encounter errors, ensure the cryptography library versions are compatible. Some libraries may not fully support Python 2.7, so you may need to troubleshoot compatibility issues or consider upgrading to Python 3 and updating dependencies accordingly
