I used the following tools to complete the homework 01-intro and created my own version using Google's Gemini Model:

1. I created directly the python file, instead of using codespace as I am having an issue accessing the elastic search localhost even if I already did the forwarding port in VS Code.

2. Podman - this is a replacement of docker. Replace the "docker" to "podman"


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Code: Run in Terminal
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
podman run -it --rm --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:9.0.1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



3. Gemini AI - Get your API Key here at google AI Studio (https://aistudio.google.com/prompts/new_chat) - click Get API Key

Note: This is a replacement for OpenAI as I am always hitting the limit. I used gemini-2.0-flash-lite as a model

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Code: Run in Python Notebook
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pip install google-generativeai
import google.generativeai as genai
genai.configure(api_key="") #--- Input your Gemini API Key
model = genai.GenerativeModel('gemini-2.0-flash-lite')
response = model.generate_content([
     {"role": "user", "parts": [q]}
])

response.text
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



4. To achieve token counting for Gemini Model:
   
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Code: Run in Python Notebook
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Get token count using the model's count_tokens method
response = model.count_tokens(prompt1)

#The response object will have a 'total_tokens' attribute
number_of_tokens = response.total_tokens
print(f"Number of tokens in the prompt: {number_of_tokens}")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
