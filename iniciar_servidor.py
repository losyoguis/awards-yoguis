from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
import webbrowser


ROOT = Path(__file__).resolve().parent


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        super().end_headers()


handler = partial(PreviewHandler, directory=str(ROOT))
server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
url = f"http://127.0.0.1:{server.server_address[1]}/index.html"
print("Premios Yoguis está disponible en:")
print(url)
print("Deja esta ventana abierta mientras usas la presentación. Presiona Ctrl+C para cerrar.")
threading.Timer(1.0, lambda: webbrowser.open(url)).start()

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServidor cerrado.")
finally:
    server.server_close()
