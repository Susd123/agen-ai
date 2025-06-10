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
