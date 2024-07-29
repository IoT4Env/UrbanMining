import { DataType } from "node-opcua";
import { OpcUaServer } from "./opcuaServerLib.js";


(async _ =>{
    const server = new OpcUaServer()

    await server.initServer();
    console.log("initialized");

    const addressSpace = server.getAddressSpace()
    const namespace = addressSpace.getOwnNamespace();


    //#region Enums definition
    const weightEnum = ["High", "Medium", "Low"]
    const weightPlatforms = namespace.addEnumerationType({
        browseName: "Weights",
        enumeration: weightEnum
    })

    //#endregion

    //#region  Type definition
    const plcType = namespace.addObjectType({
        browseName: "PlcType"
    })

    namespace.addVariable({
        browseName: "Id",
        componentOf: plcType,
        dataType: DataType.Int16,
        modellingRule: "Mandatory",
        value:{dataType: DataType.Int16, value: 24}
    })

    namespace.addVariable({
        browseName: "PowerConsuption",
        componentOf: plcType,
        dataType: DataType.Double,
        modellingRule: "Mandatory",
        value:{dataType: DataType.Double, value: 12.4}
    })
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
