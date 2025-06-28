from langchain_ollama import ChatOllama  # type: ignore
from langchain_core.tools import tool  # type: ignore

from .utils import clean_text

class LLMService:
    def __init__(self, retriever, model_name="deepseek-r1:8b"):
        self.model = ChatOllama(model=model_name)
        self.retriever = retriever

    def ask(self, input_query: str) -> str:
        docs = self.retriever.get_relevant_documents(input_query)
        if not docs:
            return "Nenhuma informação relevante foi encontrada. Tente reformular sua pergunta."
        context = "\n".join(doc.page_content for doc in docs[:5])
        prompt = f"Com base nos dados a seguir (provenientes de tabelas e PDFs), responda claramente à pergunta:\n\n{context}\n\nPergunta: {input_query}\nResposta:"
        return clean_text(self.model.invoke(prompt).content)
