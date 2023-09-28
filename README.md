# PhotoSplit

PhotoSplit App Overview:
The photosplit app provides a web interface for users to upload a photo, split it in half (top and bottom), and then download the two halves separately.

Components & Working:
Initialization & Configuration:

A Flask application is initiated.
Constants like UPLOAD_FOLDER (where the uploaded and split photos will be stored) and ALLOWED_EXTENSIONS (acceptable photo formats) are defined.
The application configuration is set to use the defined UPLOAD_FOLDER.
Utility Functions:

A utility function checks if an uploaded file has a valid extension.
Another utility function named cut_in_half is used to split the image into two halves. The split images are saved in the UPLOAD_FOLDER.
Routes:

/: The main route displays an HTML form where users can upload their photo. Upon submission, the photo is split into two halves, which can then be downloaded.
/download/<filename>: This route allows users to download the split images.
Error Handling:

In case of any exceptions or errors during the processing, the application will render an errorpage.html which displays the error message.
How to Use PhotoSplit:
Setup:

Ensure you have Python, Flask, and Pillow installed.
Create the necessary directories (uploads for storing the uploaded and split images and templates for HTML templates).
Save your Flask code in a file named app.py and the HTML templates in the templates folder.
Run the App:

Open a terminal or command prompt.
Navigate to the directory where app.py is located.
Run the command: python app.py to start the Flask application.
You should see a message indicating the server has started, usually on http://127.0.0.1:5000/.
Using the Web Interface:

Open a web browser and navigate to http://127.0.0.1:5000/.
Use the upload button or drag-and-drop to select a photo you want to split.
Click "Upload" to submit the photo.
Once processed, you'll see download links for the top and bottom halves of the image. Click on them to download the respective halves.
Error Situations:

If you try to upload a non-image file or face any other issues, you'll be redirected to an error page that provides some details about the problem.
Shutdown:

To stop the Flask server, go back to your terminal or command prompt and press Ctrl+C.
And that's a basic rundown of the photosplit app and its usage. It's a straightforward application that demonstrates the power of Flask combined with image processing using the Pillow library.
