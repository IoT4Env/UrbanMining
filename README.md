# UrbanMining

Designing a factory to gather rare materials from WEEE using OPC UA tecnology

## Technical terminology

- WEEE:\
    Waste Electrical and Electronic Equipment, as mentioned from the [European Directive numbered 2012/19/EU,](https://en.wikipedia.org/wiki/Waste_Electrical_and_Electronic_Equipment_Directive) consists of all those electrical equipment that are no longer used.
    Theese WEEE are literal GOLD MINES (which inspieres the name of the project), full of essential build materials for other electronical devices.

- Modbus TCP:\
    It is a protocol based on the RS485 serial comunication composed of a single transmit line where N clients can transmit data one at a time.
    More information on this [wikipedia](https://en.wikipedia.org/wiki/Modbus) page.\
    The protocol is used to gather information from Plcs scattered around the factory.

- Modbus and Plc addressing mapping:\
    When working with modbus and Plc, there is a crucial relationship between the two:
    | Plc Data Type     | Modbus Data Type             |
    |-------------------|------------------            |
    |Digital inputs (DI)| Input status                 |
    |Digital Outputs (DQ)| Coils                       |
    |Analog Inputs (AI)| Input registers               |
    |Analog Outputs / Memory (AQ) | Holding registers  |

    Given that the modbus client is written in python (pymodbus==3.7.0), this information is crucial to understand the right method for reading and writing variables inside the Plc

## Software used in the project

- DRAWIO:\
    This project provides designs of both the Schema of the Factory and the OPC UA Diagram which are built with the DRAWIO Software.
    In order to view the above files, DRAWIO have to be used either online or by a local installation of the Software.

- UA Modeller:\
    The OPC UA Diagram mentioned before is modelled with the UA Modeller Software.
    Usage of the UA Modeller Software is completly optional since it is a redundancy of the OPC UA Diagram.

- OPENPLC:\
    An external OPEN SOURCE project name OPENPLC simulates the PLCs found in the PlantObjects/Plcs.png file.
    The OPENPLC project is ment to be used to emulate a real industrial environment.
    So it can emulate:
    - Data collection via modbus TCP
    - Plc program (written in Structured Text, or ST)
    - Data exchange between modbus and OPC UA server

    The installation specifications can be found in this [section](#openplc-installation).

## UrbanMining specification

This project uses the OPC UA concepts to manage a Factory specialized in the WEEE decomposition with the final goal to gather rare materials, like gold and copper, to be sold to other companies that might need those materials.
Note that the mentioned Factory is an abstraction of what a real WEEE Factory could be.

## Implementation of OPC UA on the project

Whith the OPC UA Diagram as a template, it is possible to create an OPC UA server from scratch using Programming Languages like Javascript, C#, and Python.
This project uses the Javascript language for pure semplicity implemention purpouse, but any other languages mentional before is fine to obtain the same result.

## OPENPLC installation

OpenPLC download tutorials:
- [OpenPlc editor installation (Windows, Linux, MacOS)](https://www.youtube.com/watch?v=QcP2dZATJ8Q)

- [OpenPlc runtime installation (Windows, Linux, MacOS)](https://www.youtube.com/watch?v=Il0bCK5Luto)

Once OpenPLC is installed, you can use the project I'm working on by following these steps:

- Step 1:\
    Open "OpenPlc editor".

- Step 2:\
    Press ```ctrl + o``` and select the ```Plcs``` folder located in ```./UrbanMining/PlantObjects```.\
    The program setup shows in the editor.

- Step 3:\
    Click on the orange arrow to generate program for the OpenPlc runtime and save it where you like with the .st extension.

- Step 4:\
    Open the openplc runtime and upload the .st file in the Programs section (procedure is better explained on the second link provided upwards).

- Step 5:\
    Click the Start PLC button and now a PLC is up and running locally on the PC!

## PLCs variables structure

Since it is not possible to have multiple plc on the same openplc installation, the .st program uploaded in the runtime is splittend in many programs each containing a specific Plc logic.\
This approch needs a way to organize all Plc variables to avoid address conflicts.

Structure to be defined...

## Virtual environment setup (python)

Clients used in this project is written in python, which needs the opcua library to function properly.\
All the package specifications can be found in the ```requirements.txt``` file.\
Before installing the packages, the creation of a virtual environment is recommended.\
You can create the virtual environment inside the "PythonClients" folder by running the following command:\

```python3 -m venv venv```

This will create a virtual environment named "venv" with the "venv" module.\
Next, run the following command to activate the virtual environment:\

```source venv/bin/activate```

The name "venv" should be visible in the terminal inside braces like this: (venv).

With this setup, run ```pip install -r requirements.txt``` and all the packages I am currently using will be installed in your virtual environmanet.

To deactivate the virtual environment, simply type ```deactivate``` in the terminal.

To completly remove the virtual enviroment, just delete the "venv" folder.

When the virtual environment setup is ready, python clients can be started on the terminal by typing:
```python <filename>.py```
