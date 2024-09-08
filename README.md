# UrbanMining

Designing a factory to gather rare materials from WEEE using OPC UA tecnology

## Q & A

If you have any questions about the clarity of this documentation, please submit a Pull Request describing which part(s) need more explaination.

## Technical terminology

- WEEE:\
    Waste Electrical and Electronic Equipment, as mentioned from the [European Directive numbered 2012/19/EU,](https://en.wikipedia.org/wiki/Waste_Electrical_and_Electronic_Equipment_Directive) consists of all those electrical equipment that are no longer used.
    Theese WEEE are literal GOLD MINES (which inspieres the name of the project), full of essential build materials for other electronical devices.

- Modbus TCP:\
    It is a protocol based on the RS485 serial comunication composed of a single transmit line where N clients can transmit data one at a time.
    More information can be found on this [wikipedia](https://en.wikipedia.org/wiki/Modbus) page.\
    The protocol is used to gather information from Plcs scattered around the factory.

- Modbus and Plc address mapping:\
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
    Usage of the UA Modeller Software is completly optional since it is a redundancy of the OPC UA Diagram built with DRAWIO.

- OPENPLC:\
    An external OPEN SOURCE repository named OPENPLC simulates all PLCs used in this project.
    The folder holding the logic of every plc is the UrbanMining/PlantObjects/Plcs.
    The OPENPLC is used in this context to emulate a real industrial environment.
    So it can emulate:
    - Data collection via modbus TCP
    - Plc program (written in Structured Text, or ST for short)
    - Data exchange between modbus and OPC UA server
    Note that the OPC UA feature is not currently present in OPENPLC, but i have worked around it via external python script that connects to the node JS OPC UA server and populates it with data gathered through modbus TCP.

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
The way plc variables are structured is defined as follows:

### PLC name convention:

- CLENSE PLC => C
- DENSITY PLC => D
- SHREDER PLC => S
- WEIGHT PLC => W

### Other name convention:

- POWERCONSUPTION => PC
- HIGH => H
- MEDIUM => M
- LOW => L

## Plc address location logic explained

Here are some examples of possible variables location:

```
%QW404
%QW609
%QW234
```

As of now they make no sense, but hidded in the digits position resides everything needed to identify exactly what variable is associated with what plc (and also give information about variables access).

First of all, a recurrent structure for most of variables is the ```%QW``` encoding.\
This means that the variable location is configurad as output (Q => Quit) of type world (16 bits).\
The "Q" is required for the modbus to read and write the value held by the location.

Whith that out the way, lets explore the ```%QW404``` example:

    4  Represents the plc id.

So we know that we are looking to the plc whose id is 4.

    0 Indicates whenever the variables is read only, or read and write:

    EVEN => read only variable;
    ODD => read and write;

This structure is preferible over the 0-1 encoder, because we can use all digits that come after the 1.

    4 Is a serial id starting at 0 (increments by 1 for every variable)

So this is the fifth read only variable of the fourth plc.

If we take a look at the ```%QW609``` encoding, we can conclude that:
this is a the ninth read and write variable of the sixth plc.

The third examble, ```%QW234``` is a bit trickier:\
Since the third digit increments by 1 on each variable, by reaching 9 it rolls back to 0 and increments the previus digit by 2 to maintain parity.\
Whith this knowledge, we can conclude that this is the fifteenth read and write variable of the second plc.

## Platforms identification

Consult the WEEE_Schema.png to view the id number of each platform.

## Virtual environments setup (python)

Two python virtual environments, each of them in a dedicated folder, are recommended before using the project:

1. PythonClients folder:
    - Create virtual environment: ```python3 -m venv venv_clients```
    - Activate the virtual environment: ```source venv_clients/bin/activate```
    - Install requirements: ```pip install -r requirementsClient.txt```
    - Deactivate venv when finished: ```deactivate```

2. PlantObjects/SCADA folder:
    - Create virtual environment: ```python3 -m venv venv_scada```
    - Activate the virtual environment: ```source venv_scada/bin/activate```
    - Install requirements: ```pip install -r requirementsSCADA.txt```
    - Deactivate venv when finished: ```deactivate```

Now you can execute python scripts: ```python <filename>.py```
