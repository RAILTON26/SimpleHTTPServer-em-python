import http.server
import socketserver
import socket

PORT = 8000
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer((IP , PORT), Handler)
print("Servidor ativo na porta:", PORT)
print("URL -",IP,":8000")
httpd.serve_forever()
