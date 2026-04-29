from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from src.prompt import *
import os
from langchain_community.retrievers import BM25Retriever
from sentence_transformers import CrossEncoder
import re

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
GROQ_API_KEY=os.environ.get('GROQ_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=GROQ_API_KEY
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answering_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answering_chain)

def get_dynamic_k(query):
    length = len(query.split())
    if length < 5:
        return 3
    elif length < 15:
        return 5
    else:
        return 8

chat_history = []

def format_chat_history(chat_history, last_n=3):
    history = chat_history[-last_n:]
    formatted = ""
    for turn in history:
        formatted += f"User: {turn['user']} "
        formatted += f"Assistant: {turn['assistant']} "
    return formatted


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    history_text = format_chat_history(chat_history)
    final_input = history_text + " " + msg

    k = get_dynamic_k(msg)
    retriever.search_kwargs["k"] = k
    response = rag_chain.invoke({"input": final_input})
    answer = response["answer"]

    answer = re.sub(r'\s*[•]\s*(?=[A-Z])', '\n- ', answer)
    answer = re.sub(r'\s-\s(?=[A-Z])', '\n- ', answer)
    answer = re.sub(r'\n+', '\n', answer).strip()
    answer = answer.replace("\n", "<br>")
    answer = answer.replace("- ", "• ")

    chat_history.append({
        "user": msg,
        "assistant": answer
    })

    return str(answer)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)