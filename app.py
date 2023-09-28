from flask import Flask, render_template, request, send_from_directory
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            cut_in_half(filepath)
            return render_template('download.html')
    return render_template('upload.html')


def cut_in_half(image_path):
    img = Image.open(image_path)
    width, height = img.size
    top_half = (0, 0, width, height // 2)
    bottom_half = (0, height // 2, width, height)

    img_top = img.crop(top_half)
    img_bottom = img.crop(bottom_half)

    img_top.save(os.path.join(UPLOAD_FOLDER, 'top_half.jpg'))
    img_bottom.save(os.path.join(UPLOAD_FOLDER, 'bottom_half.jpg'))


@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


@app.errorhandler(Exception)
def handle_exception(e):
    # For production, you might want to log the exception
    # and show a generic error message instead.
    return render_template('errorpage.html', error_message=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
