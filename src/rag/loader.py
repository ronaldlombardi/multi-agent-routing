# src/rag/loader.py

from langchain_community.document_loaders import TextLoader
import os

def load_documents(folder_path):
    docs = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(folder_path, file), encoding="utf-8")
            docs.extend(loader.load())

    return docs