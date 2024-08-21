from flask import Flask, request, redirect, flash, render_template
from werkzeug.utils import secure_filename
from os import path, makedirs
from config import Config
import logging

app = Flask(__name__)

app.logger.setLevel(logging.INFO)
app.config["MAX_CONTENT_LENGTH"] = Config.MAX_FILE_SIZE_BYTES
app.config["SECRET_KEY"] = Config.SECRET_KEY
makedirs(Config.UPLOAD_DIRECTORY, exist_ok=True)

@app.get("/")
def get_upload_page():
    return render_template("upload.html")

@app.post("/")
def upload_files():
    if "files" not in request.files:
        return redirect(request.url)

    files = request.files.getlist("files")
    for file in files:
        if file.filename != "": 
            save_file(file)
    return redirect(request.url)

def save_file(file):
    filename = secure_filename(file.filename)
    file_path = path.join(Config.UPLOAD_DIRECTORY, filename)
    file.save(file_path)

    app.logger.info("Saved \"%s\" to %s", filename, file_path)
    flash(f"Uploaded {filename} !")

