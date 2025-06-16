I used the following tools and did the following workaround:

1. I created the python file directly in VS Code, instead of using Codespaces, as I was having an issue accessing the Elasticsearch localhost even after forwarding the port in VS Code.

2. Podman - this is a replacement for Docker. Replace "docker" with "podman".

Run in Terminal:
podman run -it --rm --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:9.0.1

3. Gemini AI - Get your API Key at Google AI Studio (https://aistudio.google.com/prompts/new_chat) - click Get API Key. Note: This is a replacement for OpenAI, as I was always hitting the limit. I used gemini-2.0-flash-lite as a model.

pip install google-generativeai
import google.generativeai as genai
genai.configure(api_key="") #--- Input your Gemini API Key
model = genai.GenerativeModel('gemini-2.0-flash-lite')
response = model.generate_content([
{"role": "user", "parts": [q]}
])
response.text

4. To achieve token counting for Gemini Model:

5. Get token count using the Gemini's model count_tokens method
response = model.count_tokens(prompt1)

The response object will have a 'total_tokens' attribute
number_of_tokens = response.total_tokens
print(f"Number of tokens in the prompt: {number_of_tokens}")
