from qtpy.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

# Initialize application
app = QApplication([])

def test_command():
    print('Plc started successfully')

# Create label and button
label = QLabel('Weight plc HMI')
button = QPushButton('Start PLC')
button.clicked.connect(test_command)

#create VERTICAL layout
layout_vertical = QVBoxLayout()
layout_vertical.addWidget(label)
layout_vertical.addWidget(button)

#create HORIZONTAL layout
layout_horizontal = QHBoxLayout()
layout_horizontal.addWidget(label)
layout_horizontal.addWidget(button)

#bind to widget parent
widget = QWidget()
widget.setLayout(layout_horizontal)
#widget.setLayout(layout_vertical)

#show widget
widget.show()

# Start 'event loop'
app.exec_()
