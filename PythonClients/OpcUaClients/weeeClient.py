import sys
sys.path.append("..")

from  opcuaClientLib import OpcuaClient
import socket


client = OpcuaClient()

hostname = socket.gethostname()

#some useful commands:
#node.get_children() -> return all node ids

#the hostname variable avoids hardcoding the hostname and adapts the content based on the pc where the server is run from
client.create_client(f"opc.tcp://{hostname}:4334/UA/UrbanMining")

if __name__ == "__main__":
    try:
        #connect to client
        client.connect()
    
        print('connected!')

        root_node = client.get_root_node()

        children = root_node.get_children()

        instances = client.get_instances()

        client.show_server_structure(instances)

    except Exception as error:
        print(error)
    finally:
        #disconnect from the server
        client.disconnect()
