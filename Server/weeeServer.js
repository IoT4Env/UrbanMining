//import { OPCUAServer, Variant, DataType, StatusCodes} from "node-opcua"
import { OpcUaServer } from "./opcuaServerLib.js";


(async _ =>{
    const server = new OpcUaServer()

    await server.initServer();
    console.log("initialized");

    const namespace = server.getOwnNamespace()

    await server.startServer()
    server.stopServerListener()
})()
