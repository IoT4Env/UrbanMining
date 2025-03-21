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
    w_plc_addresses = _json_helper.load_address_translation()["W"]
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
        self._left = 0
        self._top = 0
        self._width = 500
        self._height = 200
            
        self.set_window_title(f'Weight PLC [{JsonHelperResources.w_plc_addresses["ID"]}]')
        self.setGeometry(self._left, self._top, self._width, self._height)


        #Create main widget
        self.w_hmi = WeightHmiWidgetsLib(self)
        self.set_central_widget(self.w_hmi)

        #Show window
        self.show()


#This class creates the weight PLC HMI

class WeightHmiWidgetsLib(QtpyWidgetsLib):
    def __init__(self, parent):
        super(QtpyWidgetsLib, self).__init__(parent)

        #Store static resources for ease of use inside this class.
        self.w_plc_mb = MbClientConnection.w_plc_mb

        self.w_plc_addresses = JsonHelperResources.w_plc_addresses
        self.enumerables = JsonHelperResources.enumerables

        ##########  HMI code below  ###################
        #Create global labels
        # self.w_status_lbl = self.create_label('Status: ')
        # self.w_setting_lbl = self.create_label('Setting: ')
        # self.w_pc_lbl = self.create_label('Power consuption: ')


        #Create layout for first tab
        #self.w_plc_tab_layout = self.create_horizontal_box_layout()

        #Add created widget (w_plc) to that layout
        #self.button = self.create_push_button('test')
        #self.w_plc_tab_layout.addWidget(self.button)

        #Set layout to the first tab
        #self.w_plc_tab.setLayout(self.w_plc_tab_layout)
        #Create weight PLC tab


        #Create all required tabs
        self.tabs = self.create_tab_widget()
        self.create_w_tab()
        self.create_w_plat_l_tab()
        self.create_w_plat_m_tab()
        self.create_w_plat_h_tab()

        
        #Set tab to the main window
        self.w_plc_hmi_layout = self.create_vertical_box_layout()
        self.w_plc_hmi_layout.addWidget(self.tabs)


        #Set main widget (the one that will be shown)
        self.setLayout(self.w_plc_hmi_layout)
    
    def create_w_tab(self):
        #Create statis labels
        self.w_status_lbl = self.create_label('Status: ')
        self.w_setting_lbl = self.create_label('Setting: ')
        self.w_pc_lbl = self.create_label('Power consuption: ')


        #Create dynamic labels
        self.w_pc_mb = self.w_plc_mb.read_holding_registers(self.w_plc_addresses['PC_INT'])
        self.w_pc_value = self.create_label(f'{str(self.w_pc_mb[0])} W')
        #more stuff...


        #Create status combo box and bind event to it
        self.w_status_cb = self.create_combo_box()
        self.statuses = self.enumerables['STATUSES']

        for key, value in self.statuses.items():
            self.w_status_cb.addItem(key)
        self.w_status_cb.setCurrentIndex(self.statuses['SHUT'])

        self.bind_combobox_event(self.w_status_cb, self.w_plc_status_changed)


        #Create setting combo box and bind event to it
        self.w_setting_cb = self.create_combo_box()
        settings = self.enumerables['SETTINGS']

        for key, value in settings.items():
            self.w_setting_cb.addItem(key)
        self.w_setting_cb.setCurrentIndex(settings['MANUAL'])

        self.bind_combobox_event(self.w_setting_cb, self.w_plc_setting_changed)


        #Create weight PLC tab
        self.w_plc_tab = self.create_widget()


        #Add tabs to parent
        self.tabs.addTab(self.w_plc_tab, 'Weight PLC')


        #Create layout for weight PLC tab
        self.w_tab_layout = self.create_horizontal_box_layout()


        #Create HORIZONTAL layouts
        self.w_status_layout = self.create_horizontal_box_layout()
        self.w_status_layout.addWidget(self.w_status_lbl)
        self.w_status_layout.addWidget(self.w_status_cb)

        self.w_setting_layout = self.create_horizontal_box_layout()
        self.w_setting_layout.addWidget(self.w_setting_lbl)
        self.w_setting_layout.addWidget(self.w_setting_cb)

        self.w_pc_layout = self.create_horizontal_box_layout()
        self.w_pc_layout.addWidget(self.w_pc_lbl)
        self.w_pc_layout.addWidget(self.w_pc_value)


        #Set layouts to widget
        self.status_widget = self.create_widget()
        self.status_widget.setLayout(self.w_status_layout)

        self.setting_widget = self.create_widget()
        self.setting_widget.setLayout(self.w_setting_layout)

        self.pc_widget = self.create_widget()
        self.pc_widget.setLayout(self.w_pc_layout)


        #Create grid
        self.w_grid_layout = self.create_grid_layout()
        #widget, row_index, column_index
        self.w_grid_layout.addWidget(self.status_widget, 0, 0)
        self.w_grid_layout.addWidget(self.setting_widget, 1, 0)
        self.w_grid_layout.addWidget(self.pc_widget, 0, 1)
        #more stuff here...

        
        #Add layout / widgets to Weight PLC tab
        self.w_tab_layout.addLayout(self.w_grid_layout)

        #Set layout for the w_plc tab
        self.w_plc_tab.setLayout(self.w_tab_layout)

    def w_plc_status_changed(self):
        status = self.w_status_cb.currentText()
        self.w_plc_mb.write_register(self.w_plc_addresses['PILOT_STATUS'], self.enumerables['STATUSES'][status.upper()])
        print(f'PLC status set to: {status}')
        w_pc_mb = self.w_plc_mb.read_holding_registers(self.w_plc_addresses['PC_INT'])
        self.w_pc_value.setText(f'{str(w_pc_mb[0])} W')
    
    def w_plc_setting_changed(self):
        print('Work in progress for setting status change')


    def create_w_plat_l_tab(self):
        #Create static labels
        self.w_plat_l__status_lbl = self.create_label('Status: ')
        self.w_plat_l_setting_lbl = self.create_label('Setting: ')
        self.w_plat_l_pc_lbl = self.create_label('Power consuption: ')


        #Create dynamic labels
        self.w_pc_mb = self.w_plc_mb.read_holding_registers(self.w_plc_addresses['L']['PC_INT'])
        self.w_plat_l_pc_value = self.create_label(f'{str(self.w_pc_mb[0])} W')
        #more stuff...

        
        #Create status combo box and bind event to it
        self.w_plat_l_status_cb = self.create_combo_box()
        self.statuses = self.enumerables['STATUSES']

        for key, value in self.statuses.items():
            self.w_plat_l_status_cb.addItem(key)
        self.w_plat_l_status_cb.setCurrentIndex(self.statuses['SHUT'])

        self.bind_combobox_event(self.w_plat_l_status_cb, self.w_plat_l_status_changed)


        #Create setting combo box and bind event to it
        self.w_plat_l_setting_cb = self.create_combo_box()
        settings = self.enumerables['SETTINGS']

        for key, value in settings.items():
            self.w_plat_l_setting_cb.addItem(key)
        self.w_plat_l_setting_cb.setCurrentIndex(settings['MANUAL'])

        self.bind_combobox_event(self.w_plat_l_setting_cb, self.w_plat_l_setting_changed)


        #Create Platform Low tab
        self.w_plat_l_tab = self.create_widget()

        #Add tab to parent
        self.tabs.addTab(self.w_plat_l_tab, 'Platform_L')


        #Create layout Platform Low tab
        self.w_plat_l_tab_layout = self.create_horizontal_box_layout()


        #Create HORIZONTAL layouts
        self.w_plat_l_status_layout = self.create_horizontal_box_layout()
        self.w_plat_l_status_layout.addWidget(self.w_plat_l__status_lbl)
        self.w_plat_l_status_layout.addWidget(self.w_plat_l_status_cb)

        self.w_plat_l_setting_layout = self.create_horizontal_box_layout()
        self.w_plat_l_setting_layout.addWidget(self.w_plat_l_setting_lbl)
        self.w_plat_l_setting_layout.addWidget(self.w_plat_l_setting_cb)

        self.w_plat_l_pc_layout = self.create_horizontal_box_layout()
        self.w_plat_l_pc_layout.addWidget(self.w_plat_l_pc_lbl)
        self.w_plat_l_pc_layout.addWidget(self.w_plat_l_pc_value)


        #Set layouts to widget
        self.status_widget = self.create_widget()
        self.status_widget.setLayout(self.w_plat_l_status_layout)

        self.setting_widget = self.create_widget()
        self.setting_widget.setLayout(self.w_plat_l_setting_layout)

        self.pc_widget = self.create_widget()
        self.pc_widget.setLayout(self.w_plat_l_pc_layout)


        #Create grid
        self.w_plat_l_grid_layout = self.create_grid_layout()
        #widget, row_index, column_index
        self.w_plat_l_grid_layout.addWidget(self.status_widget, 0, 0)
        self.w_plat_l_grid_layout.addWidget(self.setting_widget, 1, 0)
        self.w_plat_l_grid_layout.addWidget(self.pc_widget, 0, 1)
        #more stuff here...

        
        #Add layout / widgets to w_plc tab
        self.w_plat_l_tab_layout.addLayout(self.w_plat_l_grid_layout)


        #Set layout for the w_plc tab
        self.w_plat_l_tab.setLayout(self.w_plat_l_tab_layout)

    
    def w_plat_l_status_changed(self):
        status = self.w_plat_l_status_cb.currentText()
        #Add PLC code for changing PC of this platform
        #self.w_plc_mb.write_register(self.w_plc_addresses['PILOT_STATUS'], self.enumerables['STATUSES'][status.upper()])
        print(f'PLC status set to: {status}')
        w_pc_mb = self.w_plc_mb.read_holding_registers(self.w_plc_addresses['L']['PC_INT'])
        self.w_pc_value.setText(f'{str(w_pc_mb[0])} W')

    def w_plat_l_setting_changed(self):
        print('Work in progress for setting status change')

    
    def create_w_plat_m_tab(self):
        self.plat_m_tab = self.create_widget()

        self.tabs.addTab(self.plat_m_tab, 'Platform_M')

    def create_w_plat_h_tab(self):
        self.plat_h_tab = self.create_widget()

        self.tabs.addTab(self.plat_h_tab, 'Platform_H')
