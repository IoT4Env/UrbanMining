from opcua import Client


class opcuaClient:

    def createClient(self, opc_url:str):
        self.client = Client(opc_url)

    def connect(self):
        self.client.connect()

    def get_root_node(self):
        return self.client.get_root_node()

    def disconnect(self):
        self.client.disconnect()