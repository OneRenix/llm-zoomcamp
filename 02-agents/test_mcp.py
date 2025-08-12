import mcp_client
import chat_assistant

our_mcp_client = mcp_client.MCPClient(["python", "weather_server.py"])

our_mcp_client.start_server()
our_mcp_client.initialize()
our_mcp_client.initialized()

mcp_tools = mcp_client.MCPTools(mcp_client=our_mcp_client)

our_mcp_client.get_tools()
our_mcp_client.call_tool('get_weather', {'city': 'Berlin'})

developer_prompt = """
You help users find out the weather in their cities. 
If they didn't specify a city, ask them. Make sure we always use a city.
""".strip()

chat_interface = chat_assistant.ChatInterface()

chat = chat_assistant.ChatAssistant(
    tools=mcp_tools,
    developer_prompt=developer_prompt,
    chat_interface=chat_interface,
    client=our_mcp_client
)

chat.run()
