# 📊 Carga Tributária LLM

Este é um projeto de demonstração de **RAG (Retrieval-Augmented Generation)** utilizando **LangChain**, **Ollama**, **FAISS** e **Streamlit** para permitir consultas inteligentes a dados tributários estruturados (CSV) e semiestruturados (PDFs).

## 🔧 Tecnologias Utilizadas

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

## 📁 Estrutura de Pastas

```
carga_tributaria_llm/
│
├── core/                      # Módulos principais do sistema
│   ├── constants.py           # Caminhos e constantes globais
│   ├── document_loader.py     # Carregamento e conversão de CSV e PDF para documentos LangChain
│   ├── vectorstore_manager.py # Indexação e carregamento do vetor FAISS
│   ├── llm_service.py         # Interface com o modelo LLM via Ollama
│   ├── utils.py               # Funções utilitárias (ex: limpeza de texto)
│
├── datasets/                  # Arquivos de dados
│   ├── *.csv                  # Tabelas tributárias
│   ├── *.pdf                  # Metadados das tabelas
│
├── faiss_datasets/            # Persistência do índice FAISS
│
├── app.py                     # Aplicação principal Streamlit
├── requirements.txt           # Dependências do projeto
├── README.md                  # Este arquivo
└── .gitignore                 # Exclusões do Git
```

## 🚀 Como Executar

### 1. Requisitos

- Python 3.10+
- Ambiente virtual configurado
- [Ollama instalado e rodando](https://ollama.com/)

### 2. Instalação

```bash
git clone https://github.com/lsprdev/carga_tributaria_llm.git
cd carga_tributaria_llm
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Executar a aplicação
```bash
streamlit run app.py
```

> O sistema irá carregar ou construir automaticamente o índice FAISS a partir dos arquivos CSV e PDF na pasta `datasets/`.

## 💡 Como Funciona?

1. Os arquivos CSV e PDF são carregados como documentos LangChain.
2. É criado um índice vetorial FAISS com embeddings via `nomic-embed-text` (Ollama).
3. O usuário digita uma pergunta na interface Streamlit.
4. O sistema busca os documentos relevantes e envia o contexto ao modelo LLM (`deepseek-r1:8b`).
5. O modelo retorna uma resposta com base nos dados.

## 📌 Observações

- O modelo precisa estar carregado localmente via Ollama (`ollama run deepseek-r1:8b`).
- O carregamento inicial pode levar alguns segundos, pois envolve leitura e indexação de documentos.
- O sistema ainda é uma prova de conceito e pode ser expandido para adicionar upload de arquivos ou histórico de respostas.