from pymodbus.client import ModbusTcpClient
import socket

slave_address = socket.gethostbyname(socket.gethostname())
port = 502

clensePlc_client = ModbusTcpClient(host=slave_address, port=port)

if __name__ == '__main__':
    clensePlc_client.connect()

    read2 = clensePlc_client.read_holding_registers(0,2)
    print(read2.registers)

    clensePlc_client.close()

