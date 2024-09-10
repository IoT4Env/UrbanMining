#External libraries
import json, sys

#go down untile the reach of root project folder
sys.path.append('../../')

#Custom libraries
from Resources import ModbusClient, ConnConfig, LoadJson


#Configure modbus connection 
modbus_connection = ConnConfig()
address = modbus_connection.host
port = modbus_connection.port

#Create LoadJson object
json_helper = LoadJson()

def load_json(path: str):
    with open(path) as f:
        return json.load(f)

#Probably better to use a separate file just in case...
def write_to_opcua():
    print('logic for inserting stuff on the opcua server')


#Code below is used to send data to the OPC UA server
if __name__ == '__main__':
    #read json for variable address translation and enumerables
    w_plc_map = json_helper.load('addressTranslation.json')['WEIGHT_PLC']
    enumerables = json_helper.load('enumerables.json')

    #Create weight plc modbus and connect to socket
    w_plc = ModbusClient(address, port)
    try:
        print(f'Now connected with {w_plc.client}')
        #Procedures to write data to the opcua server
    finally:
        w_plc.close()




    # plc_status = w_plc.read_holding_registers(w_plc_map['CURRENT_STATUS'])
    # print(f'Weight PLC status set to: {plc_status.registers}')

    # #read power consuption of plc and see that it changed!
    # plc_pc = w_plc.read_holding_registers(w_plc_map['PC_INT'])
    # print(f'Weight PLC power consuption is: {plc_pc.registers}')


    # #control platforms attached to this plc
    # #starting from the weight_h platform
    # w_plc.write_register(w_plc_map['WEIGHT_H']['STATUS'], enumerables['STATUSES']['START'])
    # weight_h_status = w_plc.read_holding_registers(w_plc_map['WEIGHT_H']['STATUS'])
    # print(f'Current status of weight high platform is: {weight_h_status.registers}')

    # #read changed power consuption
    # weight_h_pc = w_plc.read_holding_registers(w_plc_map['WEIGHT_H']['PC_INT'])
    # print(f'Weight hight power consuption is: {weight_h_pc.registers}')


