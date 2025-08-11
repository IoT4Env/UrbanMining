#External libraries
from pymodbus.client import ModbusTcpClient
import time

class ModbusClientLib:
    def __init__(self, host:str, port:int):
        self.client = ModbusTcpClient(host=host, port=port)
        self.client.connect()

    def read_holding_registers(self, address: int, count:int = 1):
        """
        Reads froma a Word data type address in the PLC.

        :param address: starting address to read.
        :param count: address to read from the starting address onwards. </br>
                        default value is 1
        """

        return self.client.read_holding_registers(address=address, count=count).registers[0:count]

    def write_register(self, address : int, value : int):
        """
        Write to a Word data type address in the PLC.

        :param address: address to write into.
        :param value: address value to set.

        """

        self.client.write_register(address=address, value=value)
        time.sleep(0.1)
    
    def read_coils(self, address : int, count : int = 1):
        """
        Reads from a Bool data type address in the PLC.

        :param address: starting address to read.
        :param count: address to read from the starting address onwards. </br>
                        default value is 1
        
        """

        return self.client.read_coils(address=address, count=count).bits[0:count]
    
    def write_coils(self, address : int, values : list[bool]):
        """
        Write to a Bool data type address in the PLC.

        :param address: address to write into.
        :param value: address value to set.
        """

        self.client.write_coils(address=address, values=values)
        #TODO: REPLACE SLEEP WITH COFFE, MEANING THAT THE PROGRAM MUST NEVER STOP FOR ANY AMOUNT OF TIME.
        time.sleep(0.1)
        
    def close(self):
        self.client.close()


