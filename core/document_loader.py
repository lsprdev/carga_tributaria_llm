import os
import pandas as pd
from langchain_core.documents import Document # type: ignore
from langchain_community.document_loaders import PyPDFLoader  # type: ignore
import streamlit as st  # type: ignore

class DocumentLoader:
    @staticmethod
    def load_csv_documents(csv_paths: list[str]) -> list[Document]:
        docs = []
        for path in csv_paths:
            try:
                df = pd.read_csv(path, sep=';', encoding='utf-8')
            except Exception as e:
                st.error(f"Erro ao ler CSV {path}: {e}")
                continue
            for idx, row in df.iterrows():
                content = "\n".join(f"{col}: {val}" for col, val in row.items())
                docs.append(Document(page_content=content, metadata={"source": os.path.basename(path), "linha": idx + 1}))
        return docs

    @staticmethod
    def load_pdf_documents(pdf_paths: list[str]) -> list[Document]:
        docs = []
        for path in pdf_paths:
            loader = PyPDFLoader(path)
            pages = loader.load()
            for page in pages:
                docs.append(Document(page_content=page.page_content, metadata={"source": os.path.basename(path)}))
        return docs
