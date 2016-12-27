import tornado.httpserver
import tornado.websocket
from tornado.ioloop import PeriodicCallback
import tornado.web
import socket

port = 9000 #Websocket Port
timeInterval= 1 #Milliseconds
global sock

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

class WSHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
		#Send message periodic via socket upon a time interval
        self.callback = PeriodicCallback(self.send_values, timeInterval)
        self.callback.start()

    def send_values(self):
        message_string, addr = sock.recvfrom(6024) # buffer size is 1024 bytes
        self.write_message(  message_string  )

    def on_message(self, message):
        pass

    def on_close(self):
        self.callback.stop()

application = tornado.web.Application([
    (r'/', WSHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
