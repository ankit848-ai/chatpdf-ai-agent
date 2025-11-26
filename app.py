import streamlit as st
from src.pdf_loader import load_pdf
from src.text_splitter import split_text
from src.embedder import embed_text
from src.vector_store import VectorStore
from src.rag_pipeline import answer_question

st.title("📄 ChatPDF AI — RAG-based PDF Question Answering")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    file_path = f"data/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

    text = load_pdf(file_path)
    st.info("PDF Loaded!")

    chunks = split_text(text)

    embeddings = embed_text(chunks)

    store = VectorStore(embedding_dim=len(embeddings[0]))
    store.add_embeddings(embeddings, chunks)

    st.success("PDF processed, now ask a question!")

    query = st.text_input("Ask your question:")

    if st.button("Get Answer"):
        answer = answer_question(query, store)
        st.write(answer)
