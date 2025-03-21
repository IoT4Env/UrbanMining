#External libraries
from qtpy.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QComboBox, QGridLayout, QTabWidget, QMainWindow
from qtpy.QtCore import Qt


################################
#Below classes are created for the purpouse of limit dependencies with the library used at the moment.
#If, in the future, this library has to be changed, only this file has to be edited since custom method names used by clients are the same.
################################


#This library is an abstraction of the official pyqt library
#The class is used by HMI python clients to build the HMI interface for the specific PLC

class QtpyWidgetsLib(QWidget):
    def __init__(self, argv : list[str] = []):
        #Create new application when instantiating object from this class
        self.qt_app = QApplication(argv)
        

    #Create function for creating a tab
    #If the client needs more tabs at once, it should use a for loop

    def create_tab(self, tab_layout, tab_name : str) -> QTabWidget:
        widget_tab = QTabWidget()

        tab = QWidget()

        tab.setLayout(tab_layout)

        widget_tab.addTab(tab, tab_name)

        return widget_tab

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
    
    def bind_combobox_event(self, combo_box : QComboBox, event):
        combo_box.currentTextChanged.connect(event)

    def bind_push_button_event(self, push_button : QPushButton, event):
        push_button.clicked.connect(event)


#This class extends the QMainWindow library
#Method names are similar to the original library method names

class QtpyMainWindowLib(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def set_window_title(self, title : str):
        return self.setWindowTitle(title)
    
    def set_central_widget(self, widget):
        return self.setCentralWidget(widget)


#This class extends the Qt enum for aligning Qt elements

class QtCoreLib:
    alignment_flags = Qt.AlignmentFlag
