from http.server import HTTPServer, BaseHTTPRequestHandler

Host = "127.0.0.1"
Port = 8080



class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_header()

        self.wfile.write(bytes("<html><body><h1>HELLO</h1></body></html>", "utf-8"))

def do_POST(self):
    self.send_response(200)
    self.send_headee("Content-type", "application/json")
    self.end_headers

server = HTTPServer((Host, Port), NeuralHTTP)
print("Server now running...")

server.serve_forever()
server.server_close()
print("Server stopp!")
         