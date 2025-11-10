# georgian-legal-rag
# ⚖️ საქართველოს სამოქალაქო კოდექსის RAG აგენტი

**Retrieval-Augmented Generation (RAG)** სისტემა, რომელიც ქართულ ენაზე პასუხობს სამართლებრივ კითხვებს **საქართველოს სამოქალაქო კოდექსის საფუძველზე**.

---

## 📘 ფუნქციები

- ამოიღებს ტექსტს PDF ფაილიდან (საქართველოს სამოქალაქო კოდექსი)
- ქმნის ტექსტის ემბედინგებს Sentence Transformers მოდელით
- ინახავს მონაცემებს ლოკალურად სწრაფი სემანტიკური ძიებისთვის
- პასუხობს ქართულად და მიუთითებს შესაბამის მუხლს/მონაკვეთს

---

## 🧠 გამოყენებული ტექნოლოგიები

- **Python 3.10+**
- **SentenceTransformers** – ტექსტის ემბედინგებისთვის  
- **FAISS** – სემანტიკური ძიებისთვის  
- **PyPDF2** – PDF ფაილიდან ტექსტის ამოსაღებად  

---

## ⚙️ ინსტალაცია

```bash
git clone https://github.com/Candie-Dev/georgian-legal-rag.git
cd georgian-legal-rag
python -m venv venv
source venv/Scripts/activate  # Windows-ზე
pip install -r requirements.txt


python extract_text.py      # კოდექსიდან ტექსტის ამოღება
python create_embeddings.py # ემბედინგების შექმნა
python rag_agent.py         # აგენტის გაშვება


👤 ავტორი

თემურ ბოლქვაძე



