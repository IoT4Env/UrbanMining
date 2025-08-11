#External libraries
import sys

#go down untile the reach of root project folder
sys.path.append('../../../')

#Custom libraries
from Resources import ModbusClientLib, ConnConfigLib, HandleJsonLib, QtpyWidgetsLib


#Configure modbus connection
modbus_connection = ConnConfigLib()
address = modbus_connection.host
port = modbus_connection.port

#Create HandleJson object
json_helper = HandleJsonLib()



#In the future might put below functions inside a class (one class for each type of HMI)
def read_initial_registers():
    #Configure modbus register reading for data gathered from this PLC
   return {
       "w_pc_mb": w_plc_mb.read_holding_registers(weight_plc_map['PC_INT'])
   } 


def go_to_platform_ui():
    #add code to change window with the specified platform data
    print('UI changed')


def w_statuses():
    status = statuses_combo_box.currentText()
    w_plc_mb.write_register(weight_plc_map['PILOT_STATUS'], enumerables['STATUSES'][status.upper()])
    print(f'PLC status set to: {status}')
    w_pc_mb = w_plc_mb.read_holding_registers(weight_plc_map['PC_INT'])
    #"w_pc_value" is defined inside main
    w_pc_value.setText(f'{str(w_pc_mb[0])} W')


if __name__ == '__main__':
    #Weight modbus connection
    w_plc_mb = ModbusClientLib(address, port)
    print(f'Now connected with {w_plc_mb.client}')
    #Connection succeded
    
    #JSON resources
    weight_plc_map = json_helper.load_json('addressTranslation.json')['WEIGHT_PLC']
    enumerables = json_helper.load_json('enumerables.json')


    #Get initial plc values
    #This approch is prefered over defining constant values at startup, because hard-coded values do not represent the real state of PLC variables
    initial_registers = read_initial_registers()
    w_pc_mb = initial_registers["w_pc_mb"]



    #Below code is the UI for the plc itself
    #Initialize weight hmi application
    w_hmi = QtpyWidgetsLib()


    #Create static labels
    w_plc = w_hmi.create_label('Weight_PLC')
    w_status = w_hmi.create_label('Status: ')
    w_setting = w_hmi.create_label('Setting: ')
    w_pc_label = w_hmi.create_label('Power consuption: ')
    
    #Create dynamic labels
    w_pc_value = w_hmi.create_label(f'{str(w_pc_mb[0])} W')
    #more stuff...

    #Create combo boxes for senting commands
    statuses_combo_box = w_hmi.create_combo_box()
    statuses = enumerables['STATUSES']
    for key, value in statuses.items():
        statuses_combo_box.addItem(key)
    statuses_combo_box.setCurrentIndex(statuses['SHUT'])

    w_hmi.bind_combobox_event(statuses_combo_box, w_statuses)

    settings_combo_box = w_hmi.create_combo_box()
    settings = enumerables['SETTINGS']
    for key, value in settings.items():
        settings_combo_box.addItem(key)
    settings_combo_box.setCurrentIndex(settings['MANUAL'])


    #Create buttons
    plat_h_button = w_hmi.create_push_button('Platform_H')
    w_hmi.bind_push_button_event(plat_h_button, go_to_platform_ui)


    plat_m_button = w_hmi.create_push_button('Platform_M')
    w_hmi.bind_push_button_event(plat_m_button, go_to_platform_ui)


    plat_l_button = w_hmi.create_push_button('Platform_L')
    w_hmi.bind_push_button_event(plat_l_button, go_to_platform_ui)


    #Create HORIZONTAL layouts
    status_layout = w_hmi.create_horizontal_box_layout()
    status_layout.addWidget(w_status)
    status_layout.addWidget(statuses_combo_box)

    setting_layout = w_hmi.create_horizontal_box_layout()
    setting_layout.addWidget(w_setting)
    setting_layout.addWidget(settings_combo_box)

    pc_layout = w_hmi.create_horizontal_box_layout()
    pc_layout.addWidget(w_pc_label)
    pc_layout.addWidget(w_pc_value)

    platforms_layout = w_hmi.create_horizontal_box_layout()
    platforms_layout.addWidget(plat_h_button)
    platforms_layout.addWidget(plat_m_button)
    platforms_layout.addWidget(plat_l_button)
    #REMENBER TO ADD VALUE OF POWER CONSUPTION!!!

    #Set layouts to widget
    status_widget = w_hmi.create_widget()
    status_widget.setLayout(status_layout)

    setting_widget = w_hmi.create_widget()
    setting_widget.setLayout(setting_layout)

    pc_widget = w_hmi.create_widget()
    pc_widget.setLayout(pc_layout)

    platforms_widget = w_hmi.create_widget()
    platforms_widget.setLayout(platforms_layout)

    #Create grid
    w_plc_grid = w_hmi.create_grid_layout()
    #widget, row_index, column_index
    w_plc_grid.addWidget(status_widget, 0, 0)
    w_plc_grid.addWidget(setting_widget, 1, 0)
    w_plc_grid.addWidget(pc_widget, 0, 1)
    #more stuff here, hopefully...

    #Combine grid and platforms
    w_plc_ui = w_hmi.create_vertical_box_layout()
    w_plc_ui.addWidget(w_plc)
    w_plc_ui.addLayout(w_plc_grid)
    w_plc_ui.addWidget(platforms_widget)

    #Set main widget
    main_widget = w_hmi.create_widget()
    main_widget.setLayout(w_plc_ui)

    #Show window
    main_widget.show()

    # Start 'event loop'
    w_hmi.start_event_loop_()

    #Close Modbus when execution finishes
    w_plc_mb.close()
    print('finished')
