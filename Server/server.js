const { OPCUAServer, Variant, DataType, StatusCodes} = require("node-opcua");

(async _ =>{
    const server = new OPCUAServer({
        port: 4334,
        resourcePath: "/UA/UrbanMining",
        buildInfo : {
            productName: "MySampleServer1",
            buildNumber: "7658",
            buildDate: new Date(2014,5,2)
        }
    });

    await server.initialize();
    console.log("initialized");

    const addressSpace = server.engine.addressSpace;
    const namespace = addressSpace.getOwnNamespace();



    await server.start();
    const endpointUrl = server.getEndpointUrl();
    console.log("Server is now listening ... ( press CTRL+C to stop)");
    console.log(" the primary server endpoint url is ", endpointUrl);

    process.once('SIGINT', async _=>{
        console.log('shutting down')
        server.shutdown()
    })
})()
