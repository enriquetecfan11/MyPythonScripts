# -*- coding: utf-8 -*-
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ChatVectorDBChain
from langchain.llms import OpenAI

from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

pdf_path = "Apple-WWDC-2023.pdf"

loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(pages, embedding=embeddings, persist_directory=".")
vectordb.persist()

pdf_qa = ChatVectorDBChain.from_llm(OpenAI(temperature=0.9, model_name="gpt-3.5-turbo"), vectordb, return_source_documents=True)

# Bucle de preguntas
while True:

    query = input("Ingrese su pregunta: ")
    result = pdf_qa({"question": query, "chat_history": ""})

    # If query is "exit" break the loop
    if query == "exit" or query == "salir":
        break

    print("--------------------------------")
    print("                                 ")
    print("Question:", query)
    print("Answer:", result["answer"])
    print("                                 ")
    print("--------------------------------")
