from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# ჩატვირთე ინდექსი და ტექსტის ნაწილები
index = faiss.read_index("civil_code.index")
chunks = np.load("chunks.npy", allow_pickle=True)
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def ask_question(question):
    q_emb = model.encode([question])
    D, I = index.search(q_emb, 3)  # 3 საუკეთესო შედეგი
    print("\n🧠 პასუხი საფუძველზე ამ მონაკვეთების:\n")
    for idx in I[0]:
        print("👉", chunks[idx][:400].replace("\n", " "), "\n")

if __name__ == "__main__":
    print("⚖️ RAG აგენტი მზადაა სამართლებრივი კითხვებისთვის.")
    while True:
        q = input("\n👉 შენი კითხვა: ")
        if q.lower() in ["გასვლა", "exit", "quit"]:
            break
        ask_question(q)
