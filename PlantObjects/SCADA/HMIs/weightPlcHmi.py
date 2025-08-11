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

def platform_ui():
    #add code to change window with the specified platform data
    print('Plc started successfully')


if __name__ == '__main__':
    #Weight modbus connection
    w_plc_mb = ModbusClientLib(address, port)
    print(f'Now connected with {w_plc_mb.client}')
    #Now we can use the modbus functionalities

    #JSON resources
    weight_plc_map = json_helper.load_json('addressTranslation.json')['WEIGHT_PLC']
    enumerables = json_helper.load_json('enumerables.json')

    #Below code is the UI for the plc itself
    #Initialize weight hmi application
    w_hmi = QtpyWidgetsLib()


    #Create labels
    w_plc = w_hmi.create_label('Weight_PLC')
    w_status = w_hmi.create_label('Status: ')
    w_setting = w_hmi.create_label('Setting: ')
    w_pc_label = w_hmi.create_label('Power consuption: ')
    #more stuff...

    #Create combo boxes for senting commands
    statuses_combo_box = w_hmi.create_combo_box()
    statuses = enumerables['STATUSES']
    for key, value in statuses.items():
        statuses_combo_box.addItem(key)
    statuses_combo_box.setCurrentIndex(statuses['SHUT'])

    def plc_statuses():
        status = statuses_combo_box.currentText()
        w_plc_mb.write_register(weight_plc_map['PILOT_STATUS'], enumerables['STATUSES'][status.upper()])
        print(f'PLC status set to: {status}')
        w_pc_mb = w_plc_mb.read_holding_registers(weight_plc_map['PC_INT'])
        w_pc_value.setText(f'{str(w_pc_mb[0])} W')


    statuses_combo_box.currentTextChanged.connect(plc_statuses)

    settings_combo_box = w_hmi.create_combo_box()
    settings = enumerables['SETTINGS']
    for key, value in settings.items():
        settings_combo_box.addItem(key)
    settings_combo_box.setCurrentIndex(settings['MANUAL'])

    #Create labels for reading data gatherd from PLC
    w_pc_mb = w_plc_mb.read_holding_registers(weight_plc_map['PC_INT'])
    w_pc_value = w_hmi.create_label(f'{str(w_pc_mb[0])} W')

    #Create buttons
    platH_button = w_hmi.create_push_button('Platform_H')
    platH_button.clicked.connect(platform_ui)

    platM_button = w_hmi.create_push_button('Platform_M')

    platL_button = w_hmi.create_push_button('Platform_L')

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
    platforms_layout.addWidget(platH_button)
    platforms_layout.addWidget(platM_button)
    platforms_layout.addWidget(platL_button)
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
