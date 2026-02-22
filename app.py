import os
from flask import Flask, request, jsonify
from rag import ingest, load_vectorstore, get_rag_chain

app = Flask(__name__)

DB_DIR = os.getenv("DB_DIR", "./db")

if not os.path.exists(DB_DIR):
  print("DB Belum ada, mulai ingest....")
  ingest()
  
vectorstore = load_vectorstore()
chain = get_rag_chain(vectorstore)

@app.route("/health", methods=['GET'])
def health():
  return jsonify({"status":"ok"})

@app.route("/ask", methods=["POST"])
def ask():
  data = request.get_json()
  if not data or "question" not in data:
    return jsonify({"error": "Field question wajib diisi"}), 400
  
  result = chain.invoke(data["question"])
  
  docs = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    ).invoke(data["question"])

  result = chain.invoke(data["question"])

  sources = list(set([
      doc.metadata.get("source", "unknown")
      for doc in docs
  ]))
  
  return jsonify({
        "question": data["question"],
        "answer": result.content,
        "sources": sources
  })

@app.route("/ingest", methods=["POST"])
def reingest():
    """Panggil endpoint ini kalau ada file MD baru ditambahkan"""
    global chain, vectorstore
    ingest()
    vectorstore = load_vectorstore()
    chain = get_rag_chain(vectorstore)
    return jsonify({"message": "✅ Index diperbarui"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)