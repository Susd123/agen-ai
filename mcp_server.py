import http.server
import urllib.parse
import urllib.request
import json

class MCPWebSearchHandler(http.server.BaseHTTPRequestHandler):
    """Simple HTTP server handler for web search."""

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != '/search':
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')
            return

        params = urllib.parse.parse_qs(parsed.query)
        query = params.get('q')
        if not query:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Missing q parameter')
            return
        query = query[0]
        results = fetch_duckduckgo(query)
        response = json.dumps(results).encode('utf-8')

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response)


def fetch_duckduckgo(query: str):
    """Fetch search results from DuckDuckGo Instant Answer API."""
    url = (
        "https://api.duckduckgo.com/?" +
        urllib.parse.urlencode({"q": query, "format": "json", "no_redirect": 1, "no_html": 1})
    )
    try:
        with urllib.request.urlopen(url) as resp:
            return json.load(resp)
    except Exception as exc:
        return {"error": str(exc)}


def run(port: int = 8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, MCPWebSearchHandler)
    print(f'Serving on port {port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='MCP web search server')
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Port to listen on',
    )
    args = parser.parse_args()

    run(port=args.port)
