import os
import ssl
import signal
import tornado.web
import tornado.ioloop
import tornado.websocket


class Handler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")
        print(self.stream.socket.version())
    def on_close(self):
        print("WebSocket closed")
    def on_message(self, message):
        print("Client said: {}".format(message))

if __name__ == "__main__":
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #ctx.options |= ssl.OP_NO_SSLv2
    #ctx.options |= ssl.OP_NO_SSLv3
    #ctx.options |= ssl.OP_NO_TLSv1
    #ctx.options |= ssl.OP_NO_TLSv1_1
    ctx.load_cert_chain("server.cert",
                        "server.key")

    app = tornado.web.Application([(r"/websocket", Handler)])
    app.listen(8888, "127.0.0.1", ssl_options=ctx)
    print ("Server started ...")
    tornado.ioloop.IOLoop.current().start()
