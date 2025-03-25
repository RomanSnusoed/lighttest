from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    file_path = r"C:\Users\38066\Dropbox\Team AI\Roman\test\ct - cf - cens.pdf"  # Укажите путь к вашему PDF-файлу
    extracted_text = extract_text_from_pdf(file_path)
    print(extracted_text)