#!/usr/bin/env python3

from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
import ssl

class ServerHandler(StreamRequestHandler):
	def handle(self):
		data = self.connection.recv(4096)
		self.wfile.write(data)

class Server(ThreadingMixIn, TCPServer):
	def __init__(self, addr, RequestHandlerClass, certfile, keyfile):
		super().__init__(addr, RequestHandlerClass, True)
		self.certfile = certfile
		self.keyfile = keyfile
		self.ssl_version = ssl.PROTOCOL_TLSv1_2

	def get_request(self):
		sock, addr = self.socket.accept()
		stream = ssl.wrap_socket(sock, server_side=True, certfile = self.certfile, keyfile = self.keyfile, ssl_version = self.ssl_version)
		return stream, addr



server = Server(("127.0.0.1", 5151), ServerHandler, "cert.pem", "key.pem")

server.serve_forever()

