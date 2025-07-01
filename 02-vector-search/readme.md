# 📚 02 - Vector Search: Homework & Setup Guide

This README documents my solution to the `02-vector-search` homework from the **LLM Zoomcamp** course. Instead of using OpenAI and Docker, I opted for **Google Gemini** and **Podman** due to API rate limits and local setup preferences.

Below, you'll find the tools, installation steps, and code snippets used throughout the project.

---

## 🛠️ Tools & Technologies

### 1. **Jupyter Notebook**
All the code and experimentation are done within a Jupyter Notebook for interactive exploration and reproducibility.

---

### 2. **Podman & Qdrant**

- **Qdrant** is used as the vector similarity search engine and database.
- **Podman** serves as a drop-in Docker replacement — all `docker` commands work by replacing `docker` with `podman`.

#### 🧱 Qdrant Setup (using Podman)
```bash
# Step 1: Pull the Qdrant image
podman pull qdrant/qdrant

# Step 2: Run Qdrant container (with named volume for persistence)
podman run -p 6333:6333 -p 6334:6334 -v qdrant_data:/qdrant/storage:z qdrant/qdrant
```

> 💡 `qdrant_data` is a named volume that Podman will manage. The actual storage path depends on your system (e.g., WSL2 on Windows).

---

### 3. **Google Gemini AI**

To avoid OpenAI rate limits, I used Google’s Gemini model (`gemini-2.5-flash`) via the **Google Generative AI** Python SDK.

#### 🔑 Get API Key
- Go to [Google AI Studio](https://aistudio.google.com/prompts/new_chat)
- Click **"Get API Key"**

#### ⚙️ Gemini Setup in Python
```bash
pip install google-generativeai
```

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-2.5-flash')

response = model.generate_content([
    {"role": "user", "parts": [q]}
])
print(response.text)
```

---

### 4. **FastEmbed**

[FastEmbed](https://github.com/xdavidhu/fastembed) is a fast and lightweight embedding library that supports various open-source models and simplifies embedding generation.

---

## ✅ Summary

This project demonstrates how to:

- Replace OpenAI with Google Gemini for LLM tasks
- Use Podman instead of Docker
- Deploy a vector database with Qdrant
- Generate embeddings using FastEmbed

---

## 📬 Questions or Feedback?

Feel free to reach out or open an issue if you have questions, suggestions, or improvements!
