from qtpy.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QComboBox, QGridLayout


#This library is an abstraction of the official pyqt library
#The class is used by HMI python clients to build the HMI interface for the specific PLC
#It should support connecting function to application events (combo-box changed, focus, etc...)

class QtpyWidgetsLib:
    def __init__(self, argv : list[str] = []):
        #Create new application when instantiating object from this class
        self.qt_app = QApplication(argv)

    def start_event_loop_(self):
        self.qt_app.exec_()

    def create_label(self, label: str) -> QLabel:
        return QLabel(label)
    
    def create_combo_box(self) -> QComboBox:
        return QComboBox()

    def create_push_button(self, btn_label : str) -> QPushButton:
        return QPushButton(btn_label)
    
    def create_vertical_box_layout(self) -> QVBoxLayout:
        return QVBoxLayout()

    def create_horizontal_box_layout(self) -> QHBoxLayout:
        return QHBoxLayout()
    
    def create_widget(self) -> QWidget:
        return QWidget()
    
    def create_grid_layout(self) -> QGridLayout:
        return QGridLayout()
