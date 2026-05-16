# 🛠️ LangChain Tools Module

---

## 🎯 What Are Tools?

Tools are the crucial bridge between Large Language Models (LLMs) and the outside world. While LLMs are great at reasoning, they are limited by their training data and cannot independently access real-time information, perform complex calculations, or interact with external systems. 

**Tools solve this by allowing agents to:**
- 🌍 Retrieve real-time data from external APIs
- 🧮 Perform deterministic mathematical calculations
- 💾 Query databases or search the web
- 🎯 Execute custom Python functions

By giving an LLM access to tools, you upgrade it from a passive text generator into an **active agent** capable of taking actions to fulfill user requests.

---

## � Updated Tools Content
This folder now includes a full currency conversion agent example that demonstrates:
- Real-time exchange rate retrieval from an external API.
- Tool chaining with LangChain, where one tool fetches a rate and another tool uses that rate for calculation.
- A practical API + calculation workflow for queries like "Convert 100 USD to INR." 

---

## �🌟 What We Built: Real-Time Currency Exchange Agent

To demonstrate the power of LangChain tools, we built a practical **Currency Conversion Agent**. This agent leverages external APIs and intelligent tool routing to answer real-world financial queries.

### How It Works

We created a system where an LLM (like Groq's Llama models) can intelligently decide when and how to convert currencies based on a user's natural language request. The workflow consists of two primary custom tools:

1. **`get_conversion_factor` (API Tool):** 
   - Takes a `base_currency` and a `target_currency`.
   - Makes a live HTTP request to the ExchangeRate-API.
   - Returns the real-time conversion rate.

2. **`convert` (Calculation Tool):** 
   - Takes the monetary amount to convert.
   - Uses LangChain's parameter injection (`InjectedToolArg`) to automatically receive the rate fetched by the first tool.
   - Accurately calculates the final converted amount.

### The Agent Workflow

When a user asks: *"Convert 100 USD to INR"*

1. **Reasoning:** The LLM analyzes the request and determines it needs real-time exchange rates to provide an accurate answer.
2. **Tool 1 Execution:** It calls the `get_conversion_factor('USD', 'INR')` tool to get the live exchange rate.
3. **Tool 2 Execution:** It then calls the `convert(100, rate)` tool, passing the amount and the newly fetched rate.
4. **Final Response:** The LLM synthesizes these mathematical and API results into a friendly, human-readable response.

---

## 💻 Code Snippets

While the full implementation is in our workspace (like `tool-calling-in-langchai.ipynb`), here is a brief look at how we defined these tools using the `@tool` decorator:

```python
from langchain_core.tools import tool, InjectedToolArg
from typing import Annotated
import requests

# Tool 1: Fetching live API data
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """Returns the real-time conversion factor from base to target currency."""
    url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/pair/{base_currency}/{target_currency}"
    return requests.get(url).json()

# Tool 2: Using injected arguments from previous tools
@tool
def convert(base_amount: float, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """Converts the amount using the injected exchange rate."""
    return base_amount * conversion_rate
```

By binding these tools to an LLM (`llm.bind_tools([get_conversion_factor, convert])`), the model autonomously manages the execution flow and parameters.

---

## 🚀 Getting Started

1. **Review the Code:** Check out the `.ipynb` and script files in the `Tools` folder for the complete currency conversion implementation, including LLM orchestration.
2. **Add Your API Key:** To test the currency exchange, ensure you have a valid API key from ExchangeRate-API.
3. **Experiment:** Try asking the agent complex queries like *"What is the conversion factor from USD to EUR, and how much is 500 USD in EUR?"* to see tool chaining in action!
