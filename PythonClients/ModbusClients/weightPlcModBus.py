from pymodbus.client import ModbusTcpClient
import socket
import time

slave_address = socket.gethostbyname(socket.gethostname())
port = 502

weightPlc_client = ModbusTcpClient(host=slave_address, port=port)

if __name__ == '__main__':
    weightPlc_client.connect()
    print(f'connected to {weightPlc_client}')

    id = weightPlc_client.read_holding_registers(3, 1)#starting at 0, read x registers
    print(f'Reading PLC id number {id.registers}')#expect to read id 3
    
    #Read power consuption when plc is closed
    pc = weightPlc_client.read_holding_registers(100, 1)
    print(f'Current power consuption: {pc.registers}')

    #Set status to Start
    weightPlc_client.write_register(110, 0)#Chnage second argument to 0 or 1 to close or start plc
    status = weightPlc_client.read_holding_registers(110, 1)#read status of first plc
    print(f'Status set to: {status.registers}')
    time.sleep(0.1)#wait some time before reading the updated value
    

    #Read power consuption and see it changed
    pc = weightPlc_client.read_holding_registers(100, 1)
    print(f'Current power consuption: {pc.registers}')

    weightPlc_client.close()

