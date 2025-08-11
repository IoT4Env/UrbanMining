#External libraries
import sys

#go down untile the reach of root project folder
sys.path.append('../../')

#Custom libraries
from Resources import OpcuaClient, ConnConfig

client = OpcuaClient()
opcua_connection = ConnConfig()

hostname = opcua_connection.host

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
