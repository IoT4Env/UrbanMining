import { OPCUAServer, Variant, DataType, StatusCodes } from "node-opcua"

export class OpcUaServer {

    constructor() {
        this.server = this.createServer()
    }

    createServer = _ => new OPCUAServer({
        port: 4334,
        resourcePath: "/UA/UrbanMining",
        buildInfo: {
            productName: "UrbanMiningServer",
            buildNumber: "7658",
            buildDate: new Date()
        }
    })

    initServer = async _ => {
        await this.server.initialize()
    }

    getAddressSpace =  _ => {
        return this.server.engine.addressSpace
    }

    startServer = async _ => {
        await this.server.start()
        const endpointUrl = this.server.getEndpointUrl();
        console.log("Server is now listening ... ( press CTRL+C to stop)");
        console.log(" the primary server endpoint url is ", endpointUrl);    
    }

    stopServerListener = _ =>{
        process.once('SIGINT', async _=>{
            console.log('shutting down')
            this.server.shutdown()
        })
    }
}
