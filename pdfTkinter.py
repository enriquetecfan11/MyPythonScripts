from tkinter import Tk, Label, Entry, Button, Scrollbar, Text, END
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ChatVectorDBChain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

pdf_path = "./tycgis/CursosTYC-GIS.pdf"

loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(pages, embedding=embeddings, persist_directory=".")
vectordb.persist()

pdf_qa = ChatVectorDBChain.from_llm(OpenAI(temperature=0.9, model_name="gpt-3.5-turbo"), vectordb, return_source_documents=True)


def buscar_respuesta():
    query = question_entry.get()
    result = pdf_qa({"question": query, "chat_history": ""})
    answer_text.delete("1.0", END)
    answer_text.insert(END, result["answer"])


root = Tk()
root.title("Chatbot PDF")
root.geometry("400x400")

question_label = Label(root, text="Pregunta:")
question_entry = Entry(root)
answer_text = Text(root, height=10, width=40)
scrollbar = Scrollbar(root)
search_button = Button(root, text="Buscar", command=buscar_respuesta)

question_label.pack()
question_entry.pack
