from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1️⃣ ჩატვირთე ტექსტი
with open("civil_code_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2️⃣ დავყოთ ტექსტი ნაწილებად (დაახლოებით 500 ასო)
chunks = [text[i:i+500] for i in range(0, len(text), 500)]

# 3️⃣ ჩატვირთე SentenceTransformer მოდელი
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

# 4️⃣ თითოეული chunk-ს ვქმნით embedding-ს
embeddings = model.encode(chunks, convert_to_numpy=True)

# 5️⃣ შევქმნათ FAISS ინდექსი
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 6️⃣ შევინახოთ ინდექსი
faiss.write_index(index, "civil_code.index")
np.save("chunks.npy", np.array(chunks))

print("✅ ემბედინგები და ინდექსი შექმნილია!")
