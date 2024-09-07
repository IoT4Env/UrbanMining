import sys
sys.path.append("..")#get modules outside of current directory

from  modbusClientLib import ModbusClient
import socket

import json


def load_json(path: str):
    with open(path) as f:
        return json.load(f)

slave_address = socket.gethostbyname(socket.gethostname())
port = 502

weight_plc = ModbusClient(slave_address, port)

if __name__ == '__main__':
    #read json for variable address translation and enumerables
    weight_plc_map = load_json('../../Resources/addressTranslation.json')['WEIGHT_PLC']
    enumerables = load_json('../../Resources/enumerables.json')

    weight_plc.connect()
    print(f'Now connected with {weight_plc.client}')

    id = weight_plc.read_holding_registers(weight_plc_map["ID"])
    print(f'Reading data from PLC number {id.registers}')

    #Set plc status to Start
    weight_plc.write_register(weight_plc_map['PILOT_STATUS'], enumerables['STATUSES']['START'])
    plc_status = weight_plc.read_holding_registers(weight_plc_map['PILOT_STATUS'])
    print(f'Weight PLC status set to: {plc_status.registers}')

    #read power consuption of plc and see that it changed!
    plc_pc = weight_plc.read_holding_registers(weight_plc_map['PC_INT'])
    print(f'Weight PLC power consuption is: {plc_pc.registers}')


    #control platforms attached to this plc
    #starting from the weight_h platform
    weight_plc.write_register(weight_plc_map['WEIGHT_H']['STATUS'], enumerables['STATUSES']['START'])
    weight_h_status = weight_plc.read_holding_registers(weight_plc_map['WEIGHT_H']['STATUS'])
    print(f'Current status of weight high platform is: {weight_h_status.registers}')

    #read changed power consuption
    weight_h_pc = weight_plc.read_holding_registers(weight_plc_map['WEIGHT_H']['PC_INT'])
    print(f'Weight hight power consuption is: {weight_h_pc.registers}')

    weight_plc.close()

