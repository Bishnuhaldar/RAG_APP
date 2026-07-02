from langchain_community.document_loaders import PyPDFLoader
import streamlit as st

FILE_PATH="/Users/ajaybiswas/Documents/RAG_APP/data/documents/Flipkart_Return_Policy.pdf"

loader=PyPDFLoader(file_path=FILE_PATH)

documents=loader.load()

st.header("This is Document loading step.")

st.write(documents)

