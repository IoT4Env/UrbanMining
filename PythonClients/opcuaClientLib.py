from opcua import Client
# from opcua import UaClient
# from opcua.client.ua_client import UaClient

#node_class identifiers:
#1 => Objects
#2 => Variables
#3 => Methods

class opcuaClient:

    def createClient(self, opc_url:str):
        self.client = Client(opc_url)

    def connect(self):
        self.client.connect()

    def get_root_node(self):
        return self.client.get_root_node()

    #get_browse_name works only on the instance (returns the name) and on properties of instance (returns the name)
    def get_instances(self):
        objects = self.client.get_objects_node()#get ALL objects inside the object node (it is a folder)
        children = objects.get_children()#get all istances inside the object node
        return children[3:len(children)]#ours instances can be found past the third element
    
    #displays the opc ua server structure
    def show_server_structure(self, instances, level=0):
        for instance in instances:
            print(f'\t' * level + f'{instance.get_browse_name().Name}:{instance.get_node_class()}')#name property is the name of the instance
            if instance.get_node_class() == 1:
                level += 1
                self.show_server_structure(instance.get_children(), level)
                level -= 1

    def disconnect(self):
        self.client.disconnect()