# 📄 ChatPDF AI — RAG-based Document Question Answering System

ChatPDF AI is an intelligent PDF question-answering system built using  
**Python, Sentence Transformers, FAISS, and Streamlit**.  
It allows users to upload any PDF and ask questions based on its content using a **RAG (Retrieval-Augmented Generation)** pipeline.

---

## 🚀 Features

- 📤 Upload any PDF  
- 📄 Automatic text extraction  
- ✂️ Smart chunking of PDF text  
- 🧠 Embedding generation using **MiniLM-L6-v2**  
- 🗄️ Fast similarity search using **FAISS**  
- 🔍 Retrieves most relevant PDF sections  
- 💬 Provides PDF-based answers  
- 🌐 Clean Streamlit UI  

---

## 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| Embedding Model | Sentence Transformers (MiniLM-L6-v2) |
| Vector Database | FAISS CPU |
| UI Framework | Streamlit |
| PDF Parsing | PyPDF |
| Math/Arrays | NumPy |

---

## 📁 Project Structure

chatpdf-ai-agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│ ├── pdf_loader.py
│ ├── text_splitter.py
│ ├── embedder.py
│ ├── vector_store.py
│ ├── rag_pipeline.py
│
└── data/
└── .gitkeep



---

## ⚙️ How It Works

### **1️⃣ PDF Upload & Text Extraction**
Reads all pages and extracts text using PyPDF.

### **2️⃣ Text Splitting**
Text is divided into overlapping chunks to improve context matching.

### **3️⃣ Embedding Generation**
Each chunk is turned into a vector using  
✔ `all-MiniLM-L6-v2` (fast + accurate).

### **4️⃣ Vector Storage with FAISS**
Embeddings are stored in FAISS for ultrafast similarity search.

### **5️⃣ Query Processing**
The user’s question is encoded → matched with closest PDF chunks.

### **6️⃣ PDF-Based Answer**
Top chunks are combined and displayed as the final answer.

---

## 📦 Installation & Setup

### **1️⃣ Clone the repository**
```bash
git clone https://github.com/ankit848-ai/chatpdf-ai-agent.git
cd chatpdf-ai-agent



2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py



🧩 Future Enhancements

Add LLM-generated concise answers

Highlight exact text from PDF

Multi-file support

Chat history

Deploy on Streamlit Cloud

👨‍💻 Author

Ankit Dash
B.Tech in DAML | Machine Learning & AI Enthusiast
GitHub: https://github.com/ankit848-ai
