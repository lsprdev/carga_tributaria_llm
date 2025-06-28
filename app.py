import streamlit as st  # type: ignore
from core import VectorstoreManager
from core import LLMService

st.set_page_config(page_title="Consulta Tributária", page_icon="📊")
st.title("📊 Consulta Inteligente aos Dados Tributários")

vectorstore = VectorstoreManager.load_or_create_vectorstore()
retriever = vectorstore.as_retriever()
llm_service = LLMService(retriever)

query = st.text_input("Faça sua pergunta sobre os dados:")

if query:
    resposta = llm_service.ask(query)
    st.markdown(resposta)
