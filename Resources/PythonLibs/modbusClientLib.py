#External libraries
from pymodbus.client import ModbusTcpClient
import time

class ModbusClient:
    def __init__(self, host:str, port:int):
        self.client = ModbusTcpClient(host=host, port=port)
        self.client.connect()

    def read_holding_registers(self, address:int, count:int = 1):
        return self.client.read_holding_registers(address=address, count=count).registers[0:count]

    def write_register(self, address, value):
        self.client.write_register(address=address, value=value)
        
    def close(self):
        self.client.close()


