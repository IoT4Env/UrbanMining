import sys
sys.path.append("..")

from  modbusClientLib import ModbusClient
import socket

import json


def load_address_translation():
    with open('../../Resources/addressTranslation.json') as f:
        return json.load(f)

slave_address = socket.gethostbyname(socket.gethostname())
port = 502

weight_plc = ModbusClient(slave_address, port)

if __name__ == '__main__':
    #read json for variable address translation
    plcs = load_address_translation()
    print(plcs['WEIGHT_PLC']['ID'])

    weight_plc.connect()
    print(f'now connected with {weight_plc.client}')

    id = weight_plc.read_holding_registers(plcs["WEIGHT_PLC"]["ID"])
    print(f'Reading data from PLC number {id.registers}')

    #Set plc status to Start
    weight_plc.write_register(110, 1)
    plc_status = weight_plc.read_holding_registers(110)
    print(f'Weight PLC status set to: {plc_status.registers}')

    #read power consuption of plc and see that it changed!
    plc_pc = weight_plc.read_holding_registers(100)
    print(f'Weight PLC power consuption is: {plc_pc.registers}')


    #control platforms attached to this plc
    #starting from the weight_h platform
    weight_plc.write_register(113, 1)
    weight_h_status = weight_plc.read_holding_registers(113)
    print(f'Current status of weight high platform is: {weight_h_status.registers}')

    #read changed power consuption
    weight_h_pc = weight_plc.read_holding_registers(102)
    print(f'Weight hight power consuption is: {weight_h_pc.registers}')

    weight_plc.close()

