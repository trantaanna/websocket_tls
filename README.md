# websocket_tls
Example of Using tornado websocket pkg.

#1. Basic websocket. There's websocket_server.py and websocket_client.py. *** Note: the websocket_client.py was a result of google search, I just needed a client to test my websocket and found this one online that suit my need.

#2. TLS secured websocket. Overwrite the open method to print TLS version used by client in communicating with websocket server. There are two examples for the websocket server (wss_server.py and wss_server_v2.py) and the one test client (wss_client.py)
