import SimpleHTTPServer
import SocketServer

PORT = 8080 #Port number set to be inputted 'localhost:8080'
#Handler that maps the directory structure to HTTP requests
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#Connection to socket with port and handler passed
httpd = SocketServer.TCPServer(("", PORT), Handler)

#Message run in background 
print "serving at port", PORT
httpd.serve_forever()


