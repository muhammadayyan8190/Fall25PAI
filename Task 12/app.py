from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

app = Flask(__name__)

# -------------------------------
# 📌 Dataset (QnA)
# -------------------------------
questions = [
    "admission open kab hain",
    "last date kya hai",
    "programs kya hain",
    "fee kitni hai",
    "hostel available hai",
    "scholarship milti hai"
]

answers = [
    "Admissions are open from June to August.",
    "The last date is 31 August.",
    "We offer BSCS, BBA, and Engineering programs.",
    "The fee is around 50,000 PKR per semester.",
    "Yes, hostel facility is available.",
    "Yes, merit-based scholarships are available."
]

# -------------------------------
# 📌 Load AI Model (MiniLM)
# -------------------------------
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# -------------------------------
# 📌 Convert Questions → Vectors
# -------------------------------
embeddings = model.encode(questions)

# -------------------------------
# 📌 Create FAISS Index
# -------------------------------
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# -------------------------------
# 📌 Chatbot Function
# -------------------------------
def get_answer(user_query):
    query_vector = model.encode([user_query])
    distances, indices = index.search(np.array(query_vector), 1)
    return answers[indices[0][0]]

# -------------------------------
# 📌 Routes
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_input = request.form["msg"]
    response = get_answer(user_input)
    return jsonify({"response": response})

# -------------------------------
# ▶️ Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)