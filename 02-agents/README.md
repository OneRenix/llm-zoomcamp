# 02-agents Homework

This repository contains my solutions and notes for the [LLM-Zoomcamp 2025 Agents Homework](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2025/0a-agents/homework.md#mcp). All work is done in a Jupyter Notebook with UV as the Python package and project manager.

---

## Table of Contents

- [Overview](#overview)
- [Preparation](#preparation)
- [Weather Agent Functions](#weather-agent-functions)
- [MCP (Model-Context Protocol)](#mcp-model-context-protocol)
- [FastMCP Installation](#fastmcp-installation)
- [Running the MCP Server](#running-the-mcp-server)
- [MCP Client Example](#mcp-client-example)
- [Screenshots & Outputs](#screenshots--outputs)
- [References](#references)

---

## Overview

This homework explores building a simple agent that interacts with weather data using custom Python functions. The agent is exposed to the LLM using the Model-Context Protocol (MCP) via a FastMCP server, allowing us to call Python functions as tools from the LLM interface.

---

## Preparation

We start by defining a function to generate (fake) weather data:

```python
import random

known_weather_data = {'berlin': 20.0}

def get_weather(city: str) -> float:
    city = city.strip().lower()
    if city in known_weather_data:
        return known_weather_data[city]
    return round(random.uniform(-5, 35), 1)
```

---

## Weather Agent Functions

Two main tools are exposed to the agent:

1. **Get Weather**
   ```python
   get_weather_tool = {
       "type": "function",
       "name": "get_weather",
       "description": "Gets the temperature for a specified city",
       "parameters": {
           "type": "object",
           "properties": {
               "city": {
                   "type": "string",
                   "description": "The name of the city, e.g. New York"
               }
           },
           "required": ["city"],
           "additionalProperties": False
       }
   }
   ```

2. **Set Weather**
   ```python
   def set_weather(city: str, temp: float) -> None:
       city = city.strip().lower()
       known_weather_data[city] = temp
       return 'OK'

   set_weather_tool = {
     "type": "function",
     "name": "set_weather",
     "description": "Updates the current weather temperature for a specific city.",
     "parameters": {
       "type": "object",
       "properties": {
         "city": {
           "type": "string",
           "description": "The name of the city, for example, 'New York' or 'London'."
         },
         "temp": {
           "type": "number",
           "description": "The temperature value to set, e.g., 20. The unit (Celsius, Fahrenheit) is determined by the tool's implementation."
         }
       },
       "required": ["city", "temp"],
       "additionalProperties": False
     }
   }
   ```

---

## MCP (Model-Context Protocol)

MCP is a protocol that allows LLMs to communicate with tools (functions, databases, etc.) using a structured interface. In this project, we expose the above weather functions to an agent using FastMCP.

---

## FastMCP Installation

I installed the FastMCP library using UV.  
**FastMCP version used:** `2.11.3`

---

## Running the MCP Server

When running the MCP server, you should see output similar to:

```
Starting MCP server 'Demo 🚀' with transport 'stdio'
```

This means the server is running and ready to accept requests over standard input/output.

---

## MCP Client Example

A sample interaction with the MCP server to get the temperature in Berlin:

**Request:**
```json
{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "get_weather", "arguments": {"city":"berlin"}}}
```

**Response:**
```json
{"jsonrpc":"2.0","id":3,"result":{"content":[{"type":"text","text":"20.0"}],"structuredContent":{"result":20.0},"isError":false}}
```

---

## Screenshots & Outputs

For more details and outputs, including tool listings and server interactions, see the notebook (`02-agents-hw.ipynb`).  
Example output of listing tools from the MCP client:

```
- Name: add
  Description: Add two numbers
--------------------
- Name: get_weather
  Description: Retrieves the temperature for a specified city.

Parameters:
    city (str): The name of the city for which to retrieve weather data.

Returns:
    float: The temperature associated with the city.
--------------------
- Name: set_weather
  Description: Sets the temperature for a specified city.

Parameters:
    city (str): The name of the city for which to set the weather data.
    temp (float): The temperature to associate with the city.

Returns:
    str: A confirmation string 'OK' indicating successful update.
--------------------
```

Screenshots are included in the notebook as attachments for reference.

---

## References

- [LLM-Zoomcamp Homework](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2025/0a-agents/homework.md#mcp)
- [FastMCP on PyPI](https://pypi.org/project/fastmcp/)
- [UV - Python Package Manager](https://github.com/astral-sh/uv)

---

**Note:**  
This notebook uses UV for package management and FastMCP for protocol implementation.  
All answers to homework questions are provided inline in the notebook in markdown cells.
