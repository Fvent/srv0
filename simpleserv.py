import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
#this will either show directory listing or index.html(if exists)
httpd = HTTPServer(('localhost',8000),SimpleHTTPRequestHandler)

httpd.serve_forever()