import os
import time
from tqdm import tqdm
from langchain_community.vectorstores import FAISS  # type: ignore
from langchain_ollama import OllamaEmbeddings  # type: ignore

from core import INDEX_PATH
from core import DocumentLoader

class VectorstoreManager:
    @staticmethod
    def index_exists(path: str) -> bool:
        return os.path.exists(os.path.join(path, "index.faiss")) and os.path.exists(os.path.join(path, "index.pkl"))

    @staticmethod
    def build_index(documents, index_path=INDEX_PATH, batch_size=20):
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        vectorstore = None
        for i in tqdm(range(0, len(documents), batch_size), desc="🔧 Gerando Embeddings"):
            batch = documents[i:i + batch_size]
            texts = [doc.page_content for doc in batch]
            metadatas = [doc.metadata for doc in batch]
            try:
                if vectorstore is None:
                    vectorstore = FAISS.from_texts(texts, embedding=embeddings, metadatas=metadatas)
                else:
                    vectorstore.add_texts(texts, metadatas=metadatas)
            except Exception as e:
                print(f"Erro no batch {i}-{i + batch_size}: {e}")
                time.sleep(5)
        vectorstore.save_local(index_path)
        return vectorstore

    @staticmethod
    def load_or_create_vectorstore():
        from core import CSV_FILES, PDF_FILES
        if not VectorstoreManager.index_exists(INDEX_PATH):
            docs = DocumentLoader.load_csv_documents(CSV_FILES) + DocumentLoader.load_pdf_documents(PDF_FILES)
            return VectorstoreManager.build_index(docs)
        else:
            return FAISS.load_local(INDEX_PATH, OllamaEmbeddings(model="nomic-embed-text"), allow_dangerous_deserialization=True)
