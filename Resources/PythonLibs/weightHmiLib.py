#Custom libraries
from Resources import ModbusClientLib, ConnConfigLib, JsonHelperLib, QtpyWidgetsLib, QtpyMainWindowLib



class MbClientConnection():
    #Modbus connection
    __modbus_connection = ConnConfigLib()
    __address = __modbus_connection.host
    __port = __modbus_connection.port
    w_plc_mb = ModbusClientLib(__address, __port)


class JsonHelperResources():
    #Create JsonHelperLib object
    _json_helper = JsonHelperLib()

    #JSON resources
    weight_plc_map = _json_helper.load_address_translation()["WEIGHT_PLC"]
    enumerables = _json_helper.load_enumerables()


#This class contains code for creating the weight plc HMI

class WeightHmiWindowLib(QtpyMainWindowLib):
    def __init__(self):
        super().__init__()

        #Connect to all required clients
        MbClientConnection()
        print('Modbus connection established')

        #Get required json resources
        JsonHelperResources()
        print('Json files loaded successfully')

        #Configure Window display
        self.set_window_title(f'Weight PLC [{JsonHelperResources.weight_plc_map["ID"]}]')

        #Create main widget
        self.w_hmi = WeightHmiWidgetsLib(self)
        self.set_central_widget(self.w_hmi)

        self.show()


#This class creates the weight PLC HMI

class WeightHmiWidgetsLib(QtpyWidgetsLib):
    def __init__(self, parent):
        super(QtpyWidgetsLib, self).__init__(parent)

        #Store static resources for ease of use inside this class.
        self.w_plc_mb = MbClientConnection.w_plc_mb

        self.weight_plc_map = JsonHelperResources.weight_plc_map
        self.enumerables = JsonHelperResources.enumerables

        ##########  HMI code below  ###################
        #Create labels
        self.w_status_lbl = self.create_label('Status: ')
        self.w_setting_lbl = self.create_label('Setting: ')
        self.w_pc_lbl = self.create_label('Power consuption: ')

        #Create dynamic labels
        self.w_pc_mb = self.w_plc_mb.read_holding_registers(self.weight_plc_map['PC_INT'])
        self.w_pc_value = self.create_label(f'{str(self.w_pc_mb[0])} W')
        #more stuff...


        #Create combo box and bind event to it
        self.statuses_combo_box = self.create_combo_box()
        self.statuses = self.enumerables['STATUSES']

        for key, value in self.statuses.items():
            self.statuses_combo_box.addItem(key)
        self.statuses_combo_box.setCurrentIndex(self.statuses['SHUT'])

        self.bind_combobox_event(self.statuses_combo_box, self.plc_statuse_change)


        #Create settings combo box and bind event to it
        self.settings_combo_box = self.create_combo_box()
        settings = self.enumerables['SETTINGS']

        for key, value in settings.items():
            self.settings_combo_box.addItem(key)
        self.settings_combo_box.setCurrentIndex(settings['MANUAL'])

        self.bind_combobox_event(self.settings_combo_box, self.plc_setting_changed)


        #Create buttons
        self.platH_button = self.create_push_button('Platform_H')

        self.platM_button = self.create_push_button('Platform_M')

        self.platL_button = self.create_push_button('Platform_L')

        #Create HORIZONTAL layouts
        self.status_layout = self.create_horizontal_box_layout()
        self.status_layout.addWidget(self.w_status_lbl)
        self.status_layout.addWidget(self.statuses_combo_box)

        self.setting_layout = self.create_horizontal_box_layout()
        self.setting_layout.addWidget(self.w_setting_lbl)
        self.setting_layout.addWidget(self.settings_combo_box)

        self.pc_layout = self.create_horizontal_box_layout()
        self.pc_layout.addWidget(self.w_pc_lbl)
        self.pc_layout.addWidget(self.w_pc_value)

        self.platforms_layout = self.create_horizontal_box_layout()
        self.platforms_layout.addWidget(self.platH_button)
        self.platforms_layout.addWidget(self.platM_button)
        self.platforms_layout.addWidget(self.platL_button)


        #Set layouts to widget
        self.status_widget = self.create_widget()
        self.status_widget.setLayout(self.status_layout)

        self.setting_widget = self.create_widget()
        self.setting_widget.setLayout(self.setting_layout)

        self.pc_widget = self.create_widget()
        self.pc_widget.setLayout(self.pc_layout)

        self.platforms_widget = self.create_widget()
        self.platforms_widget.setLayout(self.platforms_layout)

        #Create grid
        self.w_plc_grid_layout = self.create_grid_layout()
        #widget, row_index, column_index
        self.w_plc_grid_layout.addWidget(self.status_widget, 0, 0)
        self.w_plc_grid_layout.addWidget(self.setting_widget, 1, 0)
        self.w_plc_grid_layout.addWidget(self.pc_widget, 0, 1)
        #more stuff here...

        
        #Combine grid and platforms
        self.w_plc_layout = self.create_vertical_box_layout()
        self.w_plc_layout.addLayout(self.w_plc_grid_layout)
        self.w_plc_layout.addWidget(self.platforms_widget)


        #Set main widget (the one that will be shown)
        self.setLayout(self.w_plc_layout)

    
    def plc_statuse_change(self):
        status = self.statuses_combo_box.currentText()
        self.w_plc_mb.write_register(self.weight_plc_map['PILOT_STATUS'], self.enumerables['STATUSES'][status.upper()])
        print(f'PLC status set to: {status}')
        w_pc_mb = self.w_plc_mb.read_holding_registers(self.weight_plc_map['PC_INT'])
        self.w_pc_value.setText(f'{str(w_pc_mb[0])} W')
    
    def plc_setting_changed(self):
        print('Work in progress for setting status change')
