# 01-Intro: Homework and Gemini Model Setup

This document explains how I completed the Homework for `01-intro` in the `llm-zoomcamp` course. I chose to use Google's Gemini Model and Podman as alternatives to OpenAI and Docker, respectively, due to technical and API limitations. Below are the tools, steps, and code samples to help you get started.

---

## Tools & Approaches Used

1. **Python File Approach**  
   I created a Python file directly (rather than using GitHub Codespaces) because I experienced issues accessing Elasticsearch on localhost, even after forwarding the port in VS Code.

2. **Podman (as a Docker Replacement)**  
   Podman is a drop-in replacement for Docker. Simply substitute `docker` with `podman` in your CLI commands.

   **Start Elasticsearch with Podman:**
   ```sh
   podman run -it --rm --name elasticsearch \
     -p 9200:9200 -p 9300:9300 \
     -e "discovery.type=single-node" \
     -e "xpack.security.enabled=false" \
     docker.elastic.co/elasticsearch/elasticsearch:9.0.1
   ```

3. **Google Gemini AI**  
   - Get your API key from [Google AI Studio](https://aistudio.google.com/prompts/new_chat) (Click **"Get API Key"**).
   - I used the `gemini-2.0-flash-lite` model as a replacement for OpenAI, since I often hit the OpenAI usage limits.

   **Setup Gemini in a Python Notebook:**
   ```python
   pip install google-generativeai

   import google.generativeai as genai
   genai.configure(api_key="YOUR_GEMINI_API_KEY")
   model = genai.GenerativeModel('gemini-2.0-flash-lite')

   response = model.generate_content([
       {"role": "user", "parts": [q]}
   ])
   print(response.text)
   ```

4. **Token Counting with Gemini Model**  
   To count tokens for a prompt using Gemini:

   ```python
   # Get token count using the model's count_tokens method
   response = model.count_tokens(prompt1)
   number_of_tokens = response.total_tokens
   print(f"Number of tokens in the prompt: {number_of_tokens}")
   ```

---

## Notes

- **Podman** is fully compatible with most Docker workflows. If you encounter port or permission issues, consult the Podman documentation.
- **Gemini Model**: If you hit rate limits or run into quota issues, try generating a new API key or check your usage limits in Google AI Studio.

---

Feel free to reach out or open an issue if you have questions or suggestions!
