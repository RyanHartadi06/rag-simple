import os
# Load Document
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
# Split Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Embedding + save to vector store
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
# RAG Chain
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.2")
EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")
DOCS_DIR = os.getenv("DOCS_DIR", "./docs")
DB_DIR = os.getenv("DB_DIR", "./db")

# Load
def load_documents():
  """ Load semua file .md """
  
  loader = DirectoryLoader(DOCS_DIR, glob="**/*.md",loader_cls=UnstructuredMarkdownLoader, show_progress=True)
  docs = loader.load()
  
  print(f"Loaded {len(docs)} dokumen")
  return docs
# Split
def split_documents(docs):
  splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
  )
  
  chunks = splitter.split_documents(docs)
  print(f"Total chunks: {len(chunks)}")
  return chunks
  
# Embed
def build_vectorstore(chunks):
  embeddings = OllamaEmbeddings(
    model=EMBED_MODEL,
    base_url=OLLAMA_BASE_URL
  )
  
  vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_DIR
  )
  
  print("✅ Vector store berhasil dibuat dan disimpan")
  return vectorstore

# Load Vector store yang sudah ada
def load_vectorstore():
  embeddings = OllamaEmbeddings(
    model=EMBED_MODEL,
    base_url=OLLAMA_BASE_URL
  )
  vectorstore = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
  )
  print("Vector store berhasil di load")
  return vectorstore

def get_rag_chain(vectorstore):
  llm = ChatOllama(
    model=LLM_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=0.1
  )
  
  retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
  )
  prompt = ChatPromptTemplate.from_template("""
Jawab pertanyaan hanya berdasarkan konteks berikut:

<context>
{context}
</context>

Pertanyaan: {input}
""")
  
  def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
  
  rag_chain = (
    {
      "context": retriever | format_docs,
      "input": RunnablePassthrough(),
    }
    | prompt
    | llm
  )
  
  print("RAG chain siap")
  return rag_chain

def ingest():
  docs = load_documents()
  chunks = split_documents(docs)
  build_vectorstore(chunks)
  print("Ingest selesai")

if __name__ == "__main__":
  # docs = load_documents()
  # chunks = split_documents(docs)
  # vectorstore = build_vectorstore(chunks)
  vectorstore = load_vectorstore()
  chain = get_rag_chain(vectorstore)
  
  result = chain.invoke("Apa Itu Git?")
  print("Jawaban:", result.content)