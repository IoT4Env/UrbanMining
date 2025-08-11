#External libraries
from qtpy.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QComboBox, QGridLayout
import sys

#go down untile the reach of root project folder
sys.path.append('../../../')

#Custom libraries
from Resources import ModbusClient, ConnConfig, LoadJson


#Configure modbus connection
modbus_connection = ConnConfig()
address = modbus_connection.host
port = modbus_connection.port

#Create LoadJson object
json_helper = LoadJson()

def platform_ui():
    #add code to change window with the specified platform data
    print('Plc started successfully')


if __name__ == '__main__':
    #Weight modbus connection
    w_plc_mb = ModbusClient(address, port)
    print(f'Now connected with {w_plc_mb.client}')
    #Now we can use the modbus functionalities

    #JSON resources
    weight_plc_map = json_helper.load('addressTranslation.json')['WEIGHT_PLC']
    enumerables = json_helper.load('enumerables.json')

    #Below code is the UI for the plc itself
    #Initialize application
    app = QApplication([])

    #Create labels
    w_plc = QLabel('Weight_PLC')
    w_status = QLabel('Status: ')
    w_setting = QLabel('Setting: ')
    w_pc_label = QLabel('Power consuption: ')
    #more stuff...

    #Create combo boxes for senting commands
    statuses_combo_box = QComboBox()
    statuses = enumerables['STATUSES']
    for key, value in statuses.items():
        statuses_combo_box.addItem(key)
    statuses_combo_box.setCurrentIndex(statuses['SHUT'])

    settings_combo_box = QComboBox()
    settings = enumerables['SETTINGS']
    for key, value in settings.items():
        settings_combo_box.addItem(key)
    settings_combo_box.setCurrentIndex(settings['MANUAL'])

    #Create labels for reading data gatherd from PLC
    w_pc_value = QLabel()
    w_pc_mb = w_plc_mb.read_holding_registers(weight_plc_map['PC_INT'])
    w_pc_value.setText(f'{str(w_pc_mb[0])} W')

    #Create buttons
    platH_button = QPushButton('Platform_H')
    platH_button.clicked.connect(platform_ui)

    platM_button = QPushButton('Platform_M')

    platL_button = QPushButton('Platform_L')

    #Create HORIZONTAL layouts
    status_layout = QHBoxLayout()
    status_layout.addWidget(w_status)
    status_layout.addWidget(statuses_combo_box)

    setting_layout = QHBoxLayout()
    setting_layout.addWidget(w_setting)
    setting_layout.addWidget(settings_combo_box)

    pc_layout = QHBoxLayout()
    pc_layout.addWidget(w_pc_label)
    pc_layout.addWidget(w_pc_value)

    platforms_layout = QHBoxLayout()
    platforms_layout.addWidget(platH_button)
    platforms_layout.addWidget(platM_button)
    platforms_layout.addWidget(platL_button)
    #REMENBER TO ADD VALUE OF POWER CONSUPTION!!!

    #Set layouts to widget
    status_widget = QWidget()
    status_widget.setLayout(status_layout)

    setting_widget = QWidget()
    setting_widget.setLayout(setting_layout)

    pc_widget = QWidget()
    pc_widget.setLayout(pc_layout)

    platforms_widget = QWidget()
    platforms_widget.setLayout(platforms_layout)

    #Create grid
    w_plc_grid = QGridLayout()
    #widget, row_index, column_index
    w_plc_grid.addWidget(status_widget, 0, 0)
    w_plc_grid.addWidget(setting_widget, 1, 0)
    w_plc_grid.addWidget(pc_widget, 0, 1)
    #more stuff here, hopefully...

    #Combine grid and platforms
    w_plc_ui = QVBoxLayout()
    w_plc_ui.addWidget(w_plc)
    w_plc_ui.addLayout(w_plc_grid)
    w_plc_ui.addWidget(platforms_widget)

    #Set main widget
    main_widget = QWidget()
    main_widget.setLayout(w_plc_ui)

    #Show window
    main_widget.show()

    # Start 'event loop'
    app.exec_()

    #Close Modbus when execution finishes
    w_plc_mb.close()
    print('finished')
