---
tags:
  - Competition
---
https://claude.ai/chat/83bf0885-3e37-4313-ab7f-20f0bb6a1eec
https://app.trustii.io/datasets/1529

## Introduction :

While we leverage powerful models like GPT-4 and OpenAI embeddings, some use cases require a fully offline solution to ensure data sensitivity and compliance.

We invite the data science community on Trustii.io to help us create a complete offline RAG system for embeddings creation and chat/retrieval, leveraging the power of open-source technologies. 
# Objectives

**Build a Flexible Local RAG System**: Develop a RAG system that generates embeddings using an open-source LLM, the system must support local execution without relying on external API calls. The system should be **flexible** and capable of handling various types of text data, including but not limited to Q&A datasets, websites, code snippets, documentation, and more.

**Create a Versatile Local Chat Interface**: Build a chat interface that interacts with the vector store generated from text embeddings and stored locally. This interface should allow users to query embeddings and retrieve relevant information to generate responses through locally executed LLM. The interface should support interaction with different content types, multiple languages specifically handling queries in **English and French,** code snippets, etc demonstrating the system's flexibility.

## Technical Requirements :

**Local Execution**: The RAG system must run entirely locally without making external API calls to LLMs (e.g., GPT-3, GPT-4). Use open-source models for generating embeddings and text retrieval like LLAMA.

**Vector Store Implementation**:Use a vector database (must be **Faiss**) to build a vector store for efficient text retrieval. Generate embeddings using open-source LLMs (such as **LLaMA**, **Sentence Transformers**, **Mistral**) to create vectors stored in the vector store.

**Use of LangChain**: Build a chat interface using the **LangChain API**, allowing users to interact with the vector store and generate responses based on retrieved documents. The interface should demonstrate flexibility by handling various content types (text, code, websites, etc.). The chat interface must Support multiple languages, specifically English and French, for both text retrieval and response generation. The LLM must be capable of processing and generating **code snippets** and technical language.

**Programming Language**: The system must be developed in **Python**.

# Resources

https://python.langchain.com/docs/tutorials/local_rag/

https://medium.com/@vndee.huynh/build-your-own-rag-and-run-it-locally-langchain-ollama-streamlit-181d42805895

https://medium.com/@pankaj_pandey/building-a-local-rag-agent-with-llama3-and-langchain-6f041655eb83
