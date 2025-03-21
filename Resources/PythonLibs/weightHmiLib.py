#Custom libraries
from Resources import ModbusClientLib, ConnConfigLib, JsonHelperLib, QtpyWidgetsLib, QtpyMainWindowLib


#This class contains code for creating the weight plc HMI
class WeightHmiWindowLib(QtpyMainWindowLib):
    def __init__(self):
        super().__init__()

        #Get connection configurations
        self.modbus_connection = ConnConfigLib()
        self.address = self.modbus_connection.host
        self.port = self.modbus_connection.port

        #Connect to modbus client
        self.w_plc_mb = ModbusClientLib(self.address, self.port)
        print('Modbus connection established')

        #Create JsonHelperLib object
        self.json_helper = JsonHelperLib()

        #JSON resources
        self.weight_plc_map = self.json_helper.load_address_translation()["WEIGHT_PLC"]
        self.enumerables = self.json_helper.load_enumerables()

        #Configure Window display
        self.set_window_title(f'Weight PLC [{self.weight_plc_map["ID"]}]')

        #Create main widget
        self.w_hmi = WeightHmiWidgetsLib(self)
        self.set_central_widget(self.w_hmi)

        self.show()


#This class creates the weight PLC HMI

class WeightHmiWidgetsLib(QtpyWidgetsLib):
    def __init__(self, parent):
        super(QtpyWidgetsLib, self).__init__(parent)

        #HMI code below
        

