from flask import Flask, render_template, request, redirect, url_for, flash
from pdfminer.high_level import extract_text
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Для флеш-сообщений
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Создаём папку для загрузок, если её нет
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        return f"An error occurred: {e}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file part")
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("index"))

    if file:
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)  # Сохраняем файл
        extracted_text = extract_text_from_pdf(file_path)  # Извлекаем текст
        # os.remove(file_path)  # Удаление файла больше не требуется
        return f"<h1>Extracted Text:</h1><pre>{extracted_text}</pre>"

if __name__ == "__main__":
    app.run(debug=True, port=8080)