# Music Sharing App

The Music Sharing App is a web application that allows users to upload and share their music files with others. Users can upload music files, specify the access type (public, private, or protected), and optionally share the protected files with specific email addresses.

## Features

- Upload music files in various formats.
- Choose access type for uploaded music files: public, private, or protected.
- Share protected music files with specific email addresses.
- Play shared music files directly on the website.
- Display the username of the user who shared the music file.
- Delete music files.

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- Bootstrap

## Installation

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd music-sharing-app`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For Unix or Linux: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Run the development server: `python manage.py runserver`
8. Access the application in your web browser: `http://localhost:8000`

## Usage

- Register a new account or log in with an existing account.
- Upload music files using the "Upload Music" button.
- Choose the access type for each uploaded file.
- If the access type is set to "protected," enter the email addresses of the recipients.
- View and play shared music files on the home page.
- Delete music files using the "Delete" button.


