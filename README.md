# agen-ai

This repository contains a minimal MCP web search server implemented in Python.

## Running the server

```bash
python3 mcp_server.py --port 8000
```

Then send a request to search the web:

```bash
curl "http://localhost:8000/search?q=openai"
```

The server queries DuckDuckGo's Instant Answer API and returns a JSON payload
with the results. If network access is unavailable, the response will contain an
`error` field describing the failure.

## Research agent

The repository includes `research_agent.py`, a simple example using the
[AutoGen](https://github.com/microsoft/autogen) framework. The script
creates a `DeepResearchAgent` and interacts with it via a `UserProxyAgent`.
To run the agent, first provide LLM API credentials through a `.env` file
or environment variables understood by `config_list_from_dotenv()`:

```bash
OPENAI_API_KEY=sk-...
```

Then execute the script with your research question:

```bash
python3 research_agent.py "What is the tallest mountain in the world?"
```

The agent will use AutoGen to answer the question using available web tools.
