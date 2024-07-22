from  opcuaClientLib import opcuaClient 
import socket

client = opcuaClient()

hostname = socket.gethostname()

#the hostname variable avoids hardcoding the hostname and adapts the content based on the pc where the server is run from
client.createClient(f"opc.tcp://{hostname}:4334/UA/UrbanMining")

if __name__ == "__main__":
    try:
        #connect to client
        client.connect()
    
        print('connected!')

        print(client.get_root_node())

    except Exception as error:
        print(error)
    finally:
        #disconnect from the server
        client.disconnect()
