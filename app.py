from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("<h1>Hello！服务器全自动部署成功啦！</h1>".encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8001), RequestHandler)
    server.serve_forever()
