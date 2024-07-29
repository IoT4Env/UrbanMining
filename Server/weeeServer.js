import { DataType } from "node-opcua";
import { OpcUaServer } from "./opcuaServerLib.js";


(async _ =>{
    const server = new OpcUaServer()

    await server.initServer();
    console.log("initialized");

    const addressSpace = server.getAddressSpace()
    const namespace = addressSpace.getOwnNamespace();


    //#region Enums definition
    const directions = ["Forward", "Backward"]
    namespace.addEnumerationType({
        browseName: "Directions",
        enumeration: directions
    })

    const materials = ["Steel", "Copper", "Gold", "Stone", "Clay"]
    namespace.addEnumerationType({
        browseName: "Materials",
        enumeration: materials
    })

    const settings = ["Automatic", "Manual"]
    namespace.addEnumerationType({
        browseName: "Settings",
        enumeration: settings
    })
    
    const statuses = ["On", "Off", "Functioning", "Danger"]
    namespace.addEnumerationType({
        browseName: "Statuses",
        enumeration: statuses
    })

    const functionalities = ["Controller", "Separator"]
    namespace.addEnumerationType({
        browseName: "Functionalities",
        enumeration: functionalities
    })

    const weights = ["High", "Medium", "Low"]
    namespace.addEnumerationType({
        browseName: "Weights",
        enumeration: weights
    })

    //#endregion

    //#region  Type definition

    //#region PlatformType
    const platformType = namespace.addObjectType({
        browseName: "PlatformType"
    })

    namespace.addVariable({
        browseName: "Setting",
        componentOf: platformType,
        dataType: DataType.String,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "Id",
        componentOf: platformType,
        dataType: DataType.Int16,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "Status",
        componentOf: platformType,
        dataType: DataType.String,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "Direction",
        componentOf: platformType,
        dataType: DataType.String,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "PowerConsuption",
        componentOf: plcType,
        dataType: DataType.Double,
        modellingRule: "Mandatory",
    })

    namespace.addVariable({
        browseName: "WorkingMaterial",
        componentOf: platformType,
        dataType: DataType.String,
        modellingRule: "Mandatory"
    })
    //#endregion

    //#region PlcType
    const plcType = namespace.addObjectType({
        browseName: "PlcType"
    })

    namespace.addVariable({
        browseName: "Id",
        componentOf: plcType,
        dataType: DataType.Int16,
        modellingRule: "Mandatory",
        value: {dataType: DataType.Int16, value: 15}
    })

    namespace.addVariable({
        browseName: "State",
        componentOf: plcType,
        dataType: DataType.String,
        modellingRule: "Mandatory",
        value: {dataType: DataType.String, value: status[2]}
    })

    namespace.addVariable({
        browseName: "PowerConsuption",
        componentOf: plcType,
        dataType: DataType.Double,
        modellingRule: "Mandatory",
        value: {dataType: DataType.Double, value: 15.4}
    })
    //#endregion

    //#endregion

    const clensePlc = plcType.instantiate({
        browseName: "ZClensePlc",
        organizedBy: addressSpace.rootFolder.objects,
        })

    const clensePlc2 = plcType.instantiate({
        browseName: "AClensePlc2",
        organizedBy: addressSpace.rootFolder.objects,
        })


    await server.startServer()
    server.stopServerListener()
})()
