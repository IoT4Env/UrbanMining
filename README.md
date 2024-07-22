# UrbanMining

Designing a factory to gather rare materials from WEEE using OPC UA tecnology

## Technical terminology

- WEEE
    Waste Electrical and Electronic Equipment, as mentioned from the [European Directive numbered 2012/19/EU,](https://en.wikipedia.org/wiki/Waste_Electrical_and_Electronic_Equipment_Directive) consists of all those electrical equipment that are no longer used.
    Theese WEEE are literal GOLD MINES (which inspieres the name of the project), full of essential build materials for other electronical devices.

## Software used in the project

- DRAWIO
    This project provides designs of both the Schema of the Factory and the OPC UA Diagram which are built with the DRAWIO Software.
    In order to view the above files, DRAWIO have to be used either online or by a local installation of the Software.

- UA Modeller
    The OPC UA Diagram mentioned before is modelled with the UA Modeller Software.
    Usage of the UA Modeller Software is completly optional since it is a redundancy of the OPC UA Diagram.

## UrbanMining specification

This project uses the OPC UA concepts to manage a Factory specialized in the WEEE decomposition with the final goal to gather rare materials, like gold and copper, to be sold to other companies that might need those materials.
Note that the mentioned Factory is an abstraction of what a real WEEE Factory could be.

## Implementation of OPC UA on the project

Whith the OPC UA Diagram as a template, it is possible to create an OPC UA server from scratch using Programming Languages like Javascript, C#, and Python.
This project uses the Javascript language for pure semplicity implemention purpouse, but any other languages mentional before is fine to obtain the same result.

## Guide for connecting the client to the server

The client used in this project is written in python, which needs the opcua library to function properly.\
All the package specifications can be found in the ```requirements.txt``` file.\
Before installing the packages, the creation of a virtual environment is recommended.\
You can create the virtual environment inside the "Client" folder by running the following command:\

```python3 -m venv venv```

This will create a virtual environment named "venv" with the "venv" module.\
Next, run the following command to activate the virtual environment:\

```source venv/bin/activate```

The name "venv" should be visible in the terminal inside braces like this: (venv).

With this setup, run ```pip install -r requirements.txt``` and all the packages I am currently using will be installed in your virtual environmanet.\

To deactivate the virtual environment, simply type ```deactivate``` in the terminal.\

To completly remove the virtual enviroment, just delete the "venv" folder.\
