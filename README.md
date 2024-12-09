# Student-Landlord Lease Advisor

An AI-powered application that simplifies lease document analysis and enables conversational querying. Built using **Streamlit**, **LangChain**, and other cutting-edge AI technologies, this tool allows users to upload lease agreements in PDF format, extract relevant information, and query the document interactively.

---

## Table of Contents
1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Architecture](#architecture)
6. [Key Functions](#key-functions)
7. [Future Scope](#future-scope)
8. [Contributing](#contributing)
9. [License](#license)

---

## Features

- **PDF Upload and Processing:**
  - Extract text from lease agreements using PyPDF2.
- **Text Chunking:**
  - Split large text into manageable chunks with LangChain.
- **Semantic Search:**
  - Embed text using OpenAI embeddings and index them using FAISS.
- **Conversational Interface:**
  - Ask questions about the uploaded documents and get accurate answers.
- **Memory Integration:**
  - Retains context across queries for seamless conversations.

---

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **AI Framework:** LangChain
- **Text Processing:** PyPDF2
- **Vectorization:** OpenAI Embeddings, FAISS
- **Conversational AI:** ChatOpenAI, HuggingFaceHub (optional)

---

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (if using OpenAI embeddings or ChatOpenAI)
- HuggingFace API key (if using HuggingFaceHub)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/lease-advisor.git
   cd lease-advisor
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create a `.env` file in the project root and add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key
     HUGGINGFACE_API_KEY=your_huggingface_api_key
     ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Upload Documents:**
   - Use the sidebar to upload one or more lease agreements in PDF format.
   
2. **Process Documents:**
   - Click on the **Process** button to extract text and index the document.

3. **Ask Questions:**
   - Use the input box to ask questions about the uploaded document, such as:
     - *What is the termination clause in my lease?*
     - *What are the penalties for early termination?*

4. **Interactive Responses:**
   - Receive context-aware responses powered by LangChain's conversational AI.

---

## Architecture

1. **User Interaction (Frontend):**
   - Built using Streamlit for real-time document upload and querying.

2. **Backend Processing:**
   - Extract text from PDFs using PyPDF2.
   - Split text into manageable chunks with LangChain's `CharacterTextSplitter`.

3. **Semantic Search:**
   - Embed text using OpenAI embeddings.
   - Store and query embeddings using FAISS.

4. **Conversational AI:**
   - LangChain's `ConversationalRetrievalChain` enables context-aware Q&A.

---

## Key Functions

- **PDF Text Extraction:**
  Extracts text from uploaded PDF documents.
  ```python
  def get_pdf_text(pdf_docs):
      ...
  ```

- **Text Chunking:**
  Splits text into smaller chunks for embedding.
  ```python
  def get_text_chunks(text):
      ...
  ```

- **Embedding and Indexing:**
  Generates semantic embeddings and creates a searchable vector store.
  ```python
  def get_vectorstore(text_chunks):
      ...
  ```

- **Conversational Retrieval:**
  Integrates LangChain for context-aware Q&A.
  ```python
  def get_conversation_chain(vectorstore):
      ...
  ```

---

## Future Scope

- Support for multilingual lease agreements.
- Enhanced summarization of key lease terms.
- Domain-specific fine-tuning for real estate legal documents.
- Mobile-friendly interface and app integration.
- Analytics dashboard for document insights.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like additional customization or sections in the README!
