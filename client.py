#!/usr/bin/env python3

import os, socket, ssl
from common import *

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="cert.pem",
                           cert_reqs=ssl.CERT_REQUIRED,
                           ssl_version=SSL_VERSION)
ssl_sock.connect(('127.0.0.1',5151))
ssl_sock.send(bytes("Test SSL", "utf-8"))
print(ssl_sock.recv(4096))
ssl_sock.close()

