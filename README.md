# Secure-File-Storage-Website-Using-Hybrid-Cryptography

## Objective: This website offers a platform to securely upload, store, and retrieve files using a hybrid cryptography approach. </br>

# Methodology

The project is broken into two primary stages: File Storage and File Retrieval. Here's a step-by-step look at how each stage works.</br>

1. File Storage (Encryption and Upload).</br>

    Step 1: File Upload by User. </br>
    The user begins by uploading a file to the website, which will be securely stored in encrypted form.</br>
    Step 2: File Partitioning. </br>
    Once uploaded, the file is split into N parts. Partitioning the file into smaller segments enhances security by reducing the exposure of sensitive data if any 
    single part is accessed.</br>
    Step 3: Encryption with Multiple Algorithms. </br>
    Each part is then encrypted using different algorithms in a round-robin sequence (e.g., AES for Part 1, DES for Part 2, RSA for Part 3, and so on). This 
    diversity in encryption algorithms further secures the file against unauthorized decryption.</br>
    The encryption keys for each algorithm are stored in a secure manner, but only the user has access to the "master key" needed to decrypt these individual 
    encryption keys.</br>
    Step 4: Securing Encryption Keys. </br>
    The encryption keys used for each file part are encrypted with another algorithm. The user receives this "master key" as a public key, which will be necessary 
    later for decryption.</br>
    Step 5: Storage on Google Drive via API. </br>
    Each encrypted part of the file is uploaded to the user’s Google Drive account using the Google Drive API. </br>
    To organize the encrypted parts, each file upload could create a dedicated folder on Google Drive, ensuring that all parts of one file are stored together.</br>
    Step 6: Metadata Storage. </br>
    A metadata file is created, storing essential information about the encryption sequence and algorithms used for each file part. This metadata is also encrypted 
    and stored on Google Drive, ensuring it remains secure.</br>

2. File Retrieval (Decryption and Download). </br>
    Step 1: Upload the Master Key. </br>
    When a user wants to retrieve their file, they upload their master key to the website. This key is used to decrypt the individual encryption keys for each file 
    part.</br>
    Step 2: Downloading Encrypted Parts from Google Drive. </br>
    The website fetches each encrypted part from the user’s Google Drive using file IDs or folder references stored in the metadata file. </br>
    Step 3: Decrypting Each Part. </br>
    Each downloaded part is decrypted with its corresponding algorithm, using the decryption keys obtained from the master key.</br>
    Step 4: Reassembling the Original File. </br>
    After decrypting all parts, the website reassembles them into the original file, which is then made available for download by the user.</br>





# How to Run

To set up and run the website locally or on a server, follow these steps:</br>

Prerequisites</br>
Python 2.7.15 (for compatibility with some libraries) </br>
Google Cloud Credentials for accessing Google Drive API </br>
Required Packages: Listed in requirements.txt </br>
Setup and Execution </br>
Install Dependencies </br>

Step1 :Install all necessary packages, including cryptography and Google Drive API libraries.</br>
Run pip install -r requirements.txt </br>

Step2 :Google Drive API Configuration</br>
In your Google Cloud Console, enable the Google Drive API and download the credentials file (credentials.json).</br>
Place credentials.json in the project directory to allow the website to authenticate with Google Drive on behalf of the user.</br>

Step3 :Run the Web Application</br>
Execute the command python app.py to start the server.</br>
Open a browser and navigate to http://localhost:5000 (or the assigned port) to access the website.</br>

Step4: Using the Website</br>
File Upload: Go to the file upload page, choose your file, and upload it. The website will handle encryption, partitioning, and storage on Google Drive. </br>
Download and Decryption: When you want to retrieve your file, upload the master key. The site will decrypt and reassemble the file for download.</br>

Step5: Error Handling and Troubleshooting</br>
If you encounter errors, ensure the cryptography library versions are compatible. Some libraries may not fully support Python 2.7, so you may need to troubleshoot compatibility issues or consider upgrading to Python 3 and updating dependencies accordingly.</br>
