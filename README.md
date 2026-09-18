# genai-lab

Hands-on experiments and projects for learning and exploring **Generative AI**.

The repository follows a practical progression from basic LLM/API usage to **RAG, embeddings, vector databases, MCP, AI agents, semantic search, hybrid search, and natural-language query planning**.

## Topics

* LLMs and OpenAI APIs
* Chat applications and Gradio
* Tool calling
* Tokenization and low-level LLM APIs
* Quantization
* RAG fundamentals
* Embeddings and ChromaDB
* Semantic and hybrid search
* MCP (Model Context Protocol)
* Agents using MCP and RAG
* Resume search using RAG
* Natural-language-to-query generation and semantic query planning

## Repository Structure

```text
genai-lab/
│
├── *.ipynb
│   └── Experiments and hands-on learning notebooks
│
├── files/
│   └── Sample documents used by the RAG experiments
│
├── file_utils_colab.py
│   └── Reusable Google Colab utilities for reading and writing
│       text files stored in Google Drive
│
└── README.md
```

## RAG Experiments

The `files/` directory contains sample source documents used as the knowledge base for the RAG experiments.

The notebooks demonstrate the progression from basic RAG concepts to implementations using **OpenAI embeddings and ChromaDB**, followed by semantic and hybrid retrieval approaches.

## Google Colab Utility

`file_utils_colab.py` provides reusable helper functions for working with text files stored in Google Drive from Google Colab.

It includes utilities to:

* Read text files from Google Drive
* Write text files to Google Drive
* Create folders when required

The utility is intended specifically for **Google Colab** environments.

## Purpose

This is a working lab rather than a production framework. The notebooks are intended to capture experiments, implementations, and learning as I explore different GenAI concepts and patterns.


