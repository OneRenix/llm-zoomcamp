# Homework: Search Evaluation

This repository contains a Jupyter notebook (`hw.ipynb`) for evaluating various search and retrieval methods on FAQ data, as part of the [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) course.

## Overview

The notebook guides you through the process of:
- Loading and preparing FAQ documents and ground-truth data.
- Implementing different search evaluation metrics (Hit Rate, Mean Reciprocal Rank).
- Comparing traditional keyword-based search, vector search (TF-IDF + SVD), and Qdrant vector database search.
- Calculating cosine similarity for RAG (Retrieval-Augmented Generation) evaluation.

## Setup Instructions

1. **Initialize and install dependencies**  
   This notebook uses [`uv`](https://github.com/astral-sh/uv) for dependency management:
   ```bash
   uv init
   uv sync
   ```
   All required libraries are listed in `pyproject.toml`.

2. **Run the notebook**  
   Open `hw.ipynb` in Jupyter Lab/Notebook and execute the cells in order.

## Data Sources

- FAQ documents:  
  [documents-with-ids.json](https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/03-evaluation/search_evaluation/documents-with-ids.json)
- Ground-truth question-answer pairs:  
  [ground-truth-data.csv](https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/03-evaluation/search_evaluation/ground-truth-data.csv)
- RAG evaluation results:  
  [results-gpt4o-mini.csv](https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/03-evaluation/rag_evaluation/data/results-gpt4o-mini.csv)

## Key Notebooks Sections

- **Minsearch (Keyword Search):**  
  Evaluates hit rate and MRR using boosted keyword fields.

- **Vector Search (TF-IDF + SVD):**  
  Generates document embeddings and evaluates retrieval performance.

- **Qdrant Vector DB Search:**  
  Uses [Qdrant](https://qdrant.tech/) and [FastEmbed](https://github.com/ashraq/fastembed) with Jina embeddings to index and query documents.

- **Cosine Similarity:**  
  Implements cosine similarity calculations for comparing LLM-generated answers to ground-truth answers.

## Questions Answered in the Notebook

- What is the hit rate and MRR for traditional minsearch?
- How does vector search compare when using only questions vs. using both questions and answers?
- What is the performance of Qdrant vector database search?
- How to calculate cosine similarity between predicted and true answers?

## References

- [LLM Zoomcamp by DataTalksClub](https://github.com/DataTalksClub/llm-zoomcamp)
- [Minsearch](https://github.com/DataTalksClub/minsearch)
- [Qdrant](https://qdrant.tech/)
- [FastEmbed](https://github.com/ashraq/fastembed)

---

Feel free to open issues or discussions for any questions or suggestions!
