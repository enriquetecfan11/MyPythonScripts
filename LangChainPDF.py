from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ChatVectorDBChain
from langchain.llms import OpenAI

from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
from googletrans import Translator

translator = Translator()

pdf_path = "./tycgis/CursosTYC-GIS.pdf"

loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(pages, embedding=embeddings, persist_directory=".")
vectordb.persist()

pdf_qa = ChatVectorDBChain.from_llm(OpenAI(temperature=0.9, model_name="gpt-3.5-turbo"), vectordb, return_source_documents=True)

query = input("Ingrese su pregunta: ")
result = pdf_qa({"question": query, "chat_history": ""})

translated = translator.translate(result["answer"], src='en', dest='es').text

print("--------------------------------")
print("                                 ")
print("Question:", query)
print("Answer:", translated)
print("                                 ")
print("--------------------------------")
