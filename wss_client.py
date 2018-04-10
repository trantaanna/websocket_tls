from ws4py.client import WebSocketBaseClient
import json
import ssl


ws = WebSocketBaseClient(url='wss://localhost:8888/websocket', ssl_options={"cert_reqs": ssl.CERT_NONE, "ssl_version": ssl.PROTOCOL_TLSv1_2})
info = {'Type': 'Client',
            'Request': 'EnvironmentInfo'}
print("trying to connect")
ws.connect()
ws.send(json.dumps(info))
