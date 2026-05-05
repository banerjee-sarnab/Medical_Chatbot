# Medical Chatbot using Retrieval-Augmented Generation (RAG)

## Overview

This project is a production-ready medical chatbot built using a Retrieval-Augmented Generation (RAG) architecture. It enables users to ask medical-related questions and receive context-aware, accurate responses generated from a curated knowledge base.

The system integrates large language models with vector search to ensure responses are grounded in reliable medical content rather than purely generative outputs.

---

## Key Features

* Context-aware medical question answering using RAG
* Dynamic retrieval mechanism for improved relevance
* Conversational memory for handling follow-up queries
* Integration with Llama-3-8B via Groq API
* Deployed using GitHub Actions and AWS for scalability

---

## Tech Stack

### Backend

* Python, Flask
* LangChain (RAG orchestration)
* Groq API (LLM inferencing)

### Data & Retrieval

* Pinecone (vector database)
* HuggingFace embeddings
* Multi-document PDF ingestion

### Advanced Retrieval

* Dynamic Top-K retrieval

### DevOps & Deployment

* GitHub Actions (CI/CD)
* AWS (deployment environment)

---

## Architecture

The system follows a modular RAG pipeline:

User Query
→ Query Augmentation (chat history)
→ Dynamic Top-K Retrieval (Pinecone)
→ Context Injection
→ LLM Response Generation
→ Memory Update

---

## How It Works

1. User submits a query through the web interface
2. The system augments the query using recent chat history
3. Relevant documents are retrieved from Pinecone using dynamic K
4. The LLM generates a response grounded in retrieved context
5. The interaction is stored for future conversational continuity

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/banerjee-sarnab/Medical_Chatbot.git
```

### 2. Go to the Project Directory

```bash
cd Medical_Chatbot
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

## Use Case

This system is designed as a first-level assistant for users to:

* Understand symptoms
* Learn about medical conditions
* Get general health-related guidance

---
