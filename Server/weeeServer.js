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

    //#region Type definitions

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
        componentOf: platformType,
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

    //#region Weight PlatformsType
    const weightPlatformsType = namespace.addObjectType({
        browseName: "WeightPlatformsType"
    })

    namespace.addObject({
        browseName: "WeightH",
        typeDefinition: platformType,
        componentOf: weightPlatformsType,
        modellingRule: "Mandatory"
    })

    namespace.addObject({
        browseName: "WeightM",
        typeDefinition: platformType,
        componentOf: weightPlatformsType,
        modellingRule: "Mandatory"
    })

    namespace.addObject({
        browseName: "WeightL",
        typeDefinition: platformType,
        componentOf: weightPlatformsType,
        modellingRule: "Mandatory"
    })
    //#endregion

    //#region Density PlatformsType
    const densityPlatformsType = namespace.addObjectType({
        browseName: "DensityPlatformsType"
    })

    namespace.addObject({
        browseName: "DensityH",
        typeDefinition: platformType,
        componentOf: densityPlatformsType,
        modellingRule: "Mandatory"
    })

    namespace.addObject({
        browseName: "DensityM",
        typeDefinition: platformType,
        componentOf: densityPlatformsType,
        modellingRule: "Mandatory"
    })

    namespace.addObject({
        browseName: "DensityL",
        typeDefinition: platformType,
        componentOf: densityPlatformsType,
        modellingRule: "Mandatory"
    })
    //#endregion

    //#region ShreaderType
    const shreader = namespace.addObjectType({
        browseName: "Shreader"
    })

    namespace.addVariable({
        browseName: "Setting",
        componentOf: shreader,
        dataType: DataType.String,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "Id",
        componentOf: shreader,
        dataType: DataType.Int16,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "Status",
        componentOf: shreader,
        dataType: DataType.String,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "WEEEWeight",
        componentOf: shreader,
        dataType: DataType.String,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "PowerConsuption",
        componentOf: shreader,
        dataType: DataType.Double,
        modellingRule: "Mandatory"
    })
    //#endregion

    //#region PlcType
    const plcType = namespace.addObjectType({
        browseName: "PlcType"
    })

    namespace.addObject({
        browseName: "WeightPlatforms",
        componentOf: plcType,
        typeDefinition: weightPlatformsType,
        modellingRule: "Optional",
    })

    namespace.addObject({
        browseName: "DensityPlatforms",
        componentOf: plcType,
        typeDefinition: densityPlatformsType,
        modellingRule: "Optional",
    })

    namespace.addObject({
        browseName: "Shreader",
        componentOf: plcType,
        typeDefinition: shreader,
        modellingRule: "Optional",
    })

    namespace.addObject({
        browseName: "WastePlatform",
        componentOf: plcType,
        typeDefinition: platformType,
        modellingRule: "Optional",
    })

    namespace.addObject({
        browseName: "GristPlatform",
        componentOf: plcType,
        typeDefinition: platformType,
        modellingRule: "Optional",
    })

    namespace.addVariable({
        browseName: "Id",
        componentOf: plcType,
        dataType: DataType.Int16,
        modellingRule: "Mandatory",
    })

    namespace.addVariable({
        browseName: "State",
        componentOf: plcType,
        dataType: DataType.String,
        modellingRule: "Mandatory",
    })

    namespace.addVariable({
        browseName: "Functionality",
        componentOf: plcType,
        dataType: DataType.String,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "PowerConsuption",
        componentOf: plcType,
        dataType: DataType.Double,
        modellingRule: "Mandatory",
    })
    //#endregion

    //#region StoreType
    const storeType = namespace.addVariableType({
        browseName: "StoreType",
        isAbstract: true
    })
    //#endregion

    //#region WEEEStoreType
    const weeeStoreType = namespace.addVariableType({
        browseName: "WEEEStoreType",
        subtypeOf: storeType
    })

    namespace.addVariable({
        browseName: "Id",
        componentOf: weeeStoreType,
        dataType: DataType.Int16,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "Pieces",
        componentOf: weeeStoreType,
        dataType: DataType.Int64,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "GatherPeriod",
        componentOf: weeeStoreType,
        dataType: DataType.DateTime,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "StoragePeriod",
        componentOf: weeeStoreType,
        dataType: DataType.DateTime,
        modellingRule: "Mandatory"
    })
    //#endregion

    //#region MaterialStoreType
    const materialStoreType = namespace.addVariableType({
        browseName: "MaterialStoreType",
        subtypeOf: storeType
    })

    namespace.addVariable({
        browseName: "Id",
        componentOf: materialStoreType,
        dataType: DataType.Int16,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "StoragePeriod",
        componentOf: materialStoreType,
        dataType: DataType.DateTime,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "WorkingMaterial",
        componentOf: materialStoreType,
        dataType: DataType.String,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "Quantity",
        componentOf: materialStoreType,
        dataType: DataType.Double,
        modellingRule: "Mandatory"
    })
    //#endregion

    //#region SensorType
    const sensorType = namespace.addObjectType({
        browseName: "SensorType",
        isAbstract: true
    })

    namespace.addVariable({
        browseName: "Id",
        componentOf: sensorType,
        dataType: DataType.Int16,
        modellingRule: "Mandatory"
    })

    namespace.addVariable({
        browseName: "PowerConsuption",
        componentOf: sensorType,
        dataType: DataType.Double,
        modellingRule: "Mandatory"
    })
    //#endregion

    //#region PIC16F877AWeightType
    const pic16F877AWeightType = namespace.addObjectType({
        browseName: "PIC16F877AWeightType",
        subtypeOf: sensorType
    })

    namespace.addObject({
        browseName: "MainPlatform",
        componentOf: pic16F877AWeightType,
        typeDefinition: platformType,
        modellingRule: "Mandatory"
    })
    //#endregion

    //#region PIC16F877AMagneticType
    const pic16F877AMagneticType = namespace.addObjectType({
        browseName: "PIC16F877AMagneticType",
        subtypeOf: sensorType
    })

    namespace.addObject({
        browseName: "MainPlatform",
        componentOf: pic16F877AMagneticType,
        typeDefinition: platformType,
        modellingRule: "Mandatory"
    })
    //#endregion

    //#endregion

    //#region Instances

    //#region Plcs
    const clensePlc = plcType.instantiate({
        browseName: "ClensePlc",
        organizedBy: addressSpace.rootFolder.objects,
        optionals: ["DensityPlatforms", "WastePlatform"]
    })

    const densityPlc = plcType.instantiate({
        browseName: "DensityPlc",
        organizedBy: addressSpace.rootFolder.objects,
        optionals: ["DensityPlatforms", "GristPlatform"]
    })

    const monitorShreaderPlc = plcType.instantiate({
        browseName: "MonitorShreaderPlc",
        organizedBy: addressSpace.rootFolder.objects,
        optionals: ["Shreader"]
    })

    const weightPlc = plcType.instantiate({
        browseName: "WeightPLc",
        organizedBy: addressSpace.rootFolder.objects,
        optionals: ["WeightPlatforms"]
    })
    //#endregion

    //#region Storage
    const weeeContainer = weeeStoreType.instantiate({
        browseName: "WEEEContainer",
        organizedBy: addressSpace.rootFolder.objects,
    })

    const rawMaterialStorage = weeeStoreType.instantiate({
        browseName: "RawMaterialStorage",
        organizedBy: addressSpace.rootFolder.objects,
    })

    const wasteStorage = weeeStoreType.instantiate({
        browseName: "WasteStorage",
        organizedBy: addressSpace.rootFolder.objects,
    })
    //#endregion

    //#region Pics
    const weightPic = pic16F877AWeightType.instantiate({
        browseName: "WeightPic",
        organizedBy: addressSpace.rootFolder.objects,
    })

    const magneticPic = pic16F877AMagneticType.instantiate({
        browseName: "MagneticPic",
        organizedBy: addressSpace.rootFolder.objects,
    })
    //#endregion
    
    //#endregion

    await server.startServer()
    server.stopServerListener()
})()
