#This script creates an instance of the weight HMI and displays it.
import sys

#Navigate to where the Resource folder resides
sys.path.append('../../../')

from Resources import QtpyWidgetsLib, WeightHmiWindowLib


if __name__ == '__main__':
    # Instantiate weight HMI application
    w_hmi_app = QtpyWidgetsLib([])

    # Instantiate HMI window
    w_hmi = WeightHmiWindowLib()
    
    # Display HMI
    w_hmi_app.start_event_loop_()
