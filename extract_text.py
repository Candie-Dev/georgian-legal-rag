from PyPDF2 import PdfReader

# PDF ფაილის სახელი
pdf_path = "samoqalaqo_kodeqsi.pdf"
output_path = "civil_code_text.txt"

# PDF-ის წაკითხვა
reader = PdfReader(pdf_path)
text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

# ამოღებული ტექსტის შენახვა txt ფაილში
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print("✅ ტექსტი ამოღებულია და შენახულია civil_code_text.txt ფაილში!")
