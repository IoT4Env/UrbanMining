import { OpcUaServer } from "./opcuaServerLib.js";


(async _ =>{
    const server = new OpcUaServer()

    await server.initServer();
    console.log("initialized");

    const addressSpace = server.getAddressSpace()
    const namespace = addressSpace.getOwnNamespace();

    //#region  Type definition
    const plcType = namespace.addObjectType({
        browseName: "PlcType"
    })
    //#endregion


    plcType.instantiate({
        browseName: "plc1",
        organizedBy: addressSpace.rootFolder.objects
    })

    
    await server.startServer()
    server.stopServerListener()
})()
