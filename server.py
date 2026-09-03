"""
DF Application Suite - Central Portal Server
Serves the unified portal launchpad on Port 8080 (or PORT env).
"""
import http.server
import socketserver
import os
import sys

PORT = int(os.environ.get("PORT", 8080))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 60)
        print("🚀 DF Application Portal is running!")
        print(f"📍 Central Dashboard: http://localhost:{PORT}")
        print("=" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping Portal...")
            httpd.shutdown()
