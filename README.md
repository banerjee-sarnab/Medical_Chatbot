# Medical Chatbot using Retrieval-Augmented Generation (RAG)

## Overview

This project is a production-ready medical chatbot built using a Retrieval-Augmented Generation (RAG) architecture. It enables users to ask medical-related questions and receive context-aware, accurate responses generated from a curated knowledge base.

The system integrates large language models with vector search to ensure responses are grounded in reliable medical content rather than purely generative outputs.

---

## Key Features

* Context-aware medical question answering using RAG
* Dynamic retrieval mechanism for improved relevance
* Conversational memory for handling follow-up queries
* Re-ranking of retrieved documents for improved accuracy
* Integration with a high-performance LLM via Groq API
* Deployed using GitHub Actions and AWS for scalability

---

## Tech Stack

### Backend

* Python, Flask
* LangChain (RAG orchestration)
* Groq API (LLM inference)

### Data & Retrieval

* Pinecone (vector database)
* HuggingFace embeddings
* Multi-document PDF ingestion

### Advanced Retrieval

* Dynamic Top-K retrieval
* Cross-encoder re-ranking (Sentence Transformers)

### DevOps & Deployment

* GitHub Actions (CI/CD)
* AWS (deployment environment)

---

## Architecture

The system follows a modular RAG pipeline:

User Query
→ Query Augmentation (chat history)
→ Dynamic Top-K Retrieval (Pinecone)
→ Re-ranking (Cross Encoder)
→ Context Injection
→ LLM Response Generation
→ Memory Update

---

## How It Works

1. User submits a query through the web interface
2. The system augments the query using recent chat history
3. Relevant documents are retrieved from Pinecone using dynamic K
4. Retrieved results are re-ranked for better contextual relevance
5. The LLM generates a response grounded in retrieved context
6. The interaction is stored for future conversational continuity

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd <repo-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file:

```
PINECONE_API_KEY=your_key
GROQ_API_KEY=your_key
```

### 5. Run the application

```bash
python app.py
```

---

## Deployment

The application is deployed using:

* GitHub Actions for automated CI/CD pipelines
* AWS for hosting and scalability

---

## Future Enhancements

* Hybrid search (BM25 + dense retrieval)
* Multilingual and voice support
* Drug interaction and safety modules
* Personalized health profiles
* Improved UI/UX for accessibility

---

## Limitations

* Not a substitute for professional medical advice
* Responses depend on the quality and coverage of ingested data
* Requires further validation for clinical-grade deployment

---

## Use Case

This system is designed as a first-level assistant for users to:

* Understand symptoms
* Learn about medical conditions
* Get general health-related guidance

---

## Author

Developed as an end-to-end applied AI project focused on real-world deployment of RAG systems, combining machine learning, backend engineering, and MLOps practices.

---
