from pymodbus.client import ModbusTcpClient
import time

class ModbusClient:
    def __init__(self, host:str, port:int):
        self.client = ModbusTcpClient(host=host, port=port)

    def connect(self):
        self.client.connect()

    def read_holding_registers(self, address:int, count:int = 1):
        value = self.client.read_holding_registers(address=address, count=count)
        time.sleep(0.1)#wait some time
        return value

    def write_register(self, address, value):
        self.client.write_register(address=address, value=value)
        

    
    def close(self):
        self.client.close()


