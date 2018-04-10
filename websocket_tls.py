import tornado.websocket
import tornado.web
import logging
import tornado.httpserver
import ssl

class IndexPageHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("This is your response")
        self.finish()


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print ("A client connected.")
        print ("Protocol: {} and Version: {}".format(self.request.protocol, self.request.version))
        print "Value of stream.socket.Cipher(): " + str(self.get_websocket_protocol().stream.socket.cipher())
        print "Value of stream.socket.Cipher(): " + str(self.get_websocket_protocol().stream.socket.version())


    def on_message(self, message):
        print (message)
        logging.info(message)
        self.write_message("You've said: " + message)

    def on_close(self):
        logging.info("Websocket closed")
        print("Closing connection")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
           (r'/', IndexPageHandler),
           (r'/websocket', WebSocketHandler),
        ]

        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)




if __name__ == '__main__':
    ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_ctx.load_cert_chain("server.cert",
                            "server.key")

    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app, ssl_options=ssl_ctx)

    #server.listen(8888, address="0.0.0.0")
    server.listen(8888)
    #app.listen(8888)

    print("server started...")
    tornado.ioloop.IOLoop.instance().start()
    # tornado.ioloop.IOLoop.instance().stop()
