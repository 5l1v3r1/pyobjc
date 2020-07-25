# This file is generated by objective.metadata
#
# Last update: Mon Jul 13 13:33:09 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
misc.update(
    {
        "MIDIIOErrorNotification": objc.createStructType(
            "MIDIIOErrorNotification",
            b"{MIDIIOErrorNotification=iIIi}",
            ["messageID", "messageSize", "driverDevice", "errorCode"],
        ),
        "MIDIPacketList": objc.createStructType(
            "MIDIPacketList",
            b"{MIDIPacketList=I[1{MIDIPacket=QS[256C]}]}",
            ["numPackets", "packet"],
        ),
        "MIDIThruConnectionEndpoint": objc.createStructType(
            "MIDIThruConnectionEndpoint",
            b"{MIDIThruConnectionEndpoint=Ii}",
            ["endpointRef", "uniqueID"],
        ),
        "MIDIValueMap": objc.createStructType(
            "MIDIValueMap", b"{MIDIValueMap=[128C]}", ["value"]
        ),
        "MIDIPacket": objc.createStructType(
            "MIDIPacket", b"{MIDIPacket=QS[256C]}", ["timeStamp", "length", "data"]
        ),
        "MIDICIDeviceIdentification": objc.createStructType(
            "MIDICIDeviceIdentification",
            b"{MIDICIDeviceIdentification=[3C][2C][2C][4C][5C]}",
            ["manufacturer", "family", "modelNumber", "revisionLevel", "reserved"],
        ),
        "MIDIEventList": objc.createStructType(
            "MIDIEventList",
            b"{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}",
            ["protocol", "numPackets", "packet"],
        ),
        "MIDIObjectAddRemoveNotification": objc.createStructType(
            "MIDIObjectAddRemoveNotification",
            b"{MIDIObjectAddRemoveNotification=iIIiIi}",
            ["messageID", "messageSize", "parent", "parentType", "child", "childType"],
        ),
        "MIDINotification": objc.createStructType(
            "MIDINotification", b"{MIDINotification=iI}", ["messageID", "messageSize"]
        ),
        "MIDITransform": objc.createStructType(
            "MIDITransform", b"{MIDITransform=Ss}", ["transform", "param"]
        ),
        "MIDIEventPacket": objc.createStructType(
            "MIDIEventPacket",
            b"{MIDIEventPacket=QI[64I]}",
            ["timeStamp", "wordCount", "words"],
        ),
        "MIDIObjectPropertyChangeNotification": objc.createStructType(
            "MIDIObjectPropertyChangeNotification",
            b"{MIDIObjectPropertyChangeNotification=iIIi^{__CFString=}}",
            ["messageID", "messageSize", "object", "objectType", "propertyName"],
        ),
        "MIDIThruConnectionParams": objc.createStructType(
            "MIDIThruConnectionParams",
            b"{MIDIThruConnectionParams=II[8{MIDIThruConnectionEndpoint=Ii}]I[8{MIDIThruConnectionEndpoint=Ii}][16C]CCCC{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}CCCC[3C]CSS[4S]}",
            [
                "version",
                "numSources",
                "sources",
                "numDestinations",
                "destinations",
                "channelMap",
                "lowVelocity",
                "highVelocity",
                "lowNote",
                "highNote",
                "noteNumber",
                "velocity",
                "keyPressure",
                "channelPressure",
                "programChange",
                "pitchBend",
                "filterOutSysEx",
                "filterOutMTC",
                "filterOutBeatClock",
                "filterOutTuneRequest",
                "reserved2",
                "filterOutAllControls",
                "numControlTransforms",
                "numMaps",
                "reserved3",
            ],
        ),
        "MIDIControlTransform": objc.createStructType(
            "MIDIControlTransform",
            b"{MIDIControlTransform=CCSSs}",
            [
                "controlType",
                "remappedControlType",
                "controlNumber",
                "transform",
                "param",
            ],
        ),
    }
)
constants = """$MIDINetworkBonjourServiceType$MIDINetworkNotificationContactsDidChange$MIDINetworkNotificationSessionDidChange$kMIDIDriverPropertyUsesSerial$kMIDIPropertyAdvanceScheduleTimeMuSec$kMIDIPropertyCanRoute$kMIDIPropertyConnectionUniqueID$kMIDIPropertyDeviceID$kMIDIPropertyDisplayName$kMIDIPropertyDriverDeviceEditorApp$kMIDIPropertyDriverOwner$kMIDIPropertyDriverVersion$kMIDIPropertyFactoryPatchNameFile$kMIDIPropertyImage$kMIDIPropertyIsBroadcast$kMIDIPropertyIsDrumMachine$kMIDIPropertyIsEffectUnit$kMIDIPropertyIsEmbeddedEntity$kMIDIPropertyIsMixer$kMIDIPropertyIsSampler$kMIDIPropertyManufacturer$kMIDIPropertyMaxReceiveChannels$kMIDIPropertyMaxSysExSpeed$kMIDIPropertyMaxTransmitChannels$kMIDIPropertyModel$kMIDIPropertyName$kMIDIPropertyNameConfiguration$kMIDIPropertyNameConfigurationDictionary$kMIDIPropertyOffline$kMIDIPropertyPanDisruptsStereo$kMIDIPropertyPrivate$kMIDIPropertyProtocolID$kMIDIPropertyReceiveChannels$kMIDIPropertyReceivesBankSelectLSB$kMIDIPropertyReceivesBankSelectMSB$kMIDIPropertyReceivesClock$kMIDIPropertyReceivesMTC$kMIDIPropertyReceivesNotes$kMIDIPropertyReceivesProgramChanges$kMIDIPropertySingleRealtimeEntity$kMIDIPropertySupportsGeneralMIDI$kMIDIPropertySupportsMMC$kMIDIPropertySupportsShowControl$kMIDIPropertyTransmitChannels$kMIDIPropertyTransmitsBankSelectLSB$kMIDIPropertyTransmitsBankSelectMSB$kMIDIPropertyTransmitsClock$kMIDIPropertyTransmitsMTC$kMIDIPropertyTransmitsNotes$kMIDIPropertyTransmitsProgramChanges$kMIDIPropertyUniqueID$kMIDIPropertyUserPatchNameFile$"""
enums = """$MIDINetworkConnectionPolicy_Anyone@2$MIDINetworkConnectionPolicy_HostsInContactList@1$MIDINetworkConnectionPolicy_NoOne@0$kMIDIControlType_14Bit@1$kMIDIControlType_14BitNRPN@5$kMIDIControlType_14BitRPN@3$kMIDIControlType_7Bit@0$kMIDIControlType_7BitNRPN@4$kMIDIControlType_7BitRPN@2$kMIDIIDNotUnique@-10843$kMIDIInvalidClient@-10830$kMIDIInvalidPort@-10831$kMIDIInvalidUniqueID@0$kMIDIMessageSendErr@-10838$kMIDIMsgIOError@7$kMIDIMsgObjectAdded@2$kMIDIMsgObjectRemoved@3$kMIDIMsgPropertyChanged@4$kMIDIMsgSerialPortOwnerChanged@6$kMIDIMsgSetupChanged@1$kMIDIMsgThruConnectionsChanged@5$kMIDINoConnection@-10833$kMIDINoCurrentSetup@-10837$kMIDINotPermitted@-10844$kMIDIObjectNotFound@-10842$kMIDIObjectType_Destination@3$kMIDIObjectType_Device@0$kMIDIObjectType_Entity@1$kMIDIObjectType_ExternalDestination@19$kMIDIObjectType_ExternalDevice@16$kMIDIObjectType_ExternalEntity@17$kMIDIObjectType_ExternalMask@16$kMIDIObjectType_ExternalSource@18$kMIDIObjectType_Other@-1$kMIDIObjectType_Source@2$kMIDIProtocol_1_0@1$kMIDIProtocol_2_0@2$kMIDIServerStartErr@-10839$kMIDISetupFormatErr@-10840$kMIDIThruConnection_MaxEndpoints@8$kMIDITransform_Add@8$kMIDITransform_FilterOut@1$kMIDITransform_MapControl@2$kMIDITransform_MapValue@12$kMIDITransform_MaxValue@11$kMIDITransform_MinValue@10$kMIDITransform_None@0$kMIDITransform_Scale@9$kMIDIUnknownEndpoint@-10834$kMIDIUnknownError@-10845$kMIDIUnknownProperty@-10835$kMIDIWrongEndpointType@-10832$kMIDIWrongPropertyType@-10836$kMIDIWrongThread@-10841$"""
misc.update({})
functions = {
    "MIDIObjectSetDictionaryProperty": (b"iI^{__CFString=}^{__CFDictionary=}",),
    "MIDIThruConnectionParamsInitialize": (
        b"v^{MIDIThruConnectionParams=II[8{MIDIThruConnectionEndpoint=Ii}]I[8{MIDIThruConnectionEndpoint=Ii}][16C]CCCC{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}CCCC[3C]CSS[4S]}",
        "",
        {"arguments": {0: {"type_modifier": "n"}}},
    ),
    "MIDIReceived": (b"iI^{MIDIPacketList=I[1{MIDIPacket=QS[256C]}]}",),
    "MIDIGetDriverDeviceList": (
        b"I^^{MIDIDriverInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?}",
    ),
    "MIDIPortDisconnectSource": (b"iII",),
    "MIDIObjectSetDataProperty": (b"iI^{__CFString=}^{__CFData=}",),
    "MIDISetupDispose": (b"iI",),
    "MIDISetupFromData": (
        b"i^{__CFData=}^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "MIDIGetSerialPortDrivers": (
        b"i^^{__CFArray=}",
        "",
        {"arguments": {0: {"already_cfretained": True, "type_modifier": "o"}}},
    ),
    "MIDISend": (b"iII^{MIDIPacketList=I[1{MIDIPacket=QS[256C]}]}",),
    "MIDISetupRemoveDevice": (b"iI",),
    "MIDIPacketListInit": (
        b"^{MIDIPacket=QS[256C]}^{MIDIPacketList=I[1{MIDIPacket=QS[256C]}]}",
    ),
    "MIDIDeviceGetNumberOfEntities": (b"QI",),
    "MIDIEventListInit": (
        b"^{MIDIEventPacket=QI[64I]}^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}i",
    ),
    "MIDIEntityGetNumberOfDestinations": (b"QI",),
    "MIDIThruConnectionFind": (
        b"i^{__CFString=}^^{__CFData=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "MIDIDeviceNewEntity": (
        b"iI^{__CFString=}iZQQ^I",
        "",
        {"arguments": {6: {"type_modifier": "o"}}},
    ),
    "MIDISetupAddDevice": (b"iI",),
    "MIDIGetNumberOfExternalDevices": (b"Q",),
    "MIDIGetNumberOfDevices": (b"Q",),
    "MIDIObjectRemoveProperty": (b"iI^{__CFString=}",),
    "MIDIInputPortCreate": (
        b"iI^{__CFString=}^?^v^I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{MIDIPacketList=I[1{MIDIPacket=QS[256C]}]}"},
                            1: {"type": b"^v"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "MIDISetupAddExternalDevice": (b"iI",),
    "MIDIPortConnectSource": (b"iII^v",),
    "MIDISendEventList": (b"iII^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}",),
    "MIDIPacketListAdd": (
        b"^{MIDIPacket=QS[256C]}^{MIDIPacketList=I[1{MIDIPacket=QS[256C]}]}Q^{MIDIPacket=QS[256C]}QQ^C",
    ),
    "MIDIObjectSetStringProperty": (b"iI^{__CFString=}^{__CFString=}",),
    "MIDIObjectGetDictionaryProperty": (b"iI^{__CFString=}^^{__CFDictionary=}",),
    "MIDIFlushOutput": (b"iI",),
    "MIDIClientDispose": (b"iI",),
    "MIDISetupToData": (
        b"iI^^{__CFData=}",
        "",
        {"arguments": {1: {"already_cfretained": True, "type_modifier": "o"}}},
    ),
    "MIDIDeviceDispose": (b"iI",),
    "MIDIDeviceListGetDevice": (b"IIQ",),
    "MIDIEntityAddOrRemoveEndpoints": (b"iIQQ",),
    "MIDIDestinationCreateWithBlock": (
        b"iI^{__CFString=}^I@?",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MIDIGetSource": (b"IQ",),
    "MIDIEndpointGetEntity": (b"iI^I",),
    "MIDIObjectGetIntegerProperty": (b"iI^{__CFString=}^i",),
    "MIDIThruConnectionParamsSize": (
        b"Q^{MIDIThruConnectionParams=II[8{MIDIThruConnectionEndpoint=Ii}]I[8{MIDIThruConnectionEndpoint=Ii}][16C]CCCC{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}{MIDITransform=Ss}CCCC[3C]CSS[4S]}",
    ),
    "MIDIGetDestination": (b"IQ",),
    "MIDIDestinationCreate": (
        b"iI^{__CFString=}^?^v^I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{MIDIPacketList=I[1{MIDIPacket=QS[256C]}]}"},
                            1: {"type": b"^v"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "MIDIDriverEnableMonitoring": (
        b"i^^{MIDIDriverInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?}Z",
    ),
    "MIDIObjectGetProperties": (b"iI^@Z",),
    "MIDISetupGetCurrent": (b"i^I", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "MIDIObjectGetDataProperty": (b"iI^{__CFString=}^^{__CFData=}",),
    "MIDISetupCreate": (b"i^I", "", {"retval": {"already_cfretained": True}}),
    "MIDIEndpointDispose": (b"iI",),
    "MIDIExternalDeviceCreate": (
        b"i^{__CFString=}^{__CFString=}^{__CFString=}^I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"type_modifier": "o"}},
        },
    ),
    "MIDISetSerialPortOwner": (b"i^{__CFString=}^{__CFString=}",),
    "MIDIClientCreate": (
        b"i^{__CFString=}^?^v^I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{MIDINotification=iI}"},
                            1: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "MIDIPacketNext": (b"^{MIDIPacket=QS[256C]}^{MIDIPacket=QS[256C]}",),
    "MIDIDeviceAddEntity": (
        b"iI^{__CFString=}ZQQ^I",
        "",
        {"arguments": {5: {"type_modifier": "o"}}},
    ),
    "MIDIThruConnectionDispose": (b"iI",),
    "MIDISetupInstall": (b"iI",),
    "MIDISetupRemoveExternalDevice": (b"iI",),
    "MIDIObjectFindByUniqueID": (b"ii^I^i",),
    "MIDIObjectSetIntegerProperty": (b"iI^{__CFString=}i",),
    "MIDIEventPacketNext": (b"^{MIDIEventPacket=QI[64I]}^{MIDIEventPacket=QI[64I]}",),
    "MIDIPortDispose": (b"iI",),
    "MIDIDeviceListAddDevice": (b"iII",),
    "MIDIGetNumberOfDestinations": (b"Q",),
    "MIDIRestart": (b"i",),
    "MIDIClientCreateWithBlock": (
        b"i^{__CFString=}^I@?",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MIDIThruConnectionGetParams": (
        b"iI^^{__CFData=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "MIDIEntityGetDevice": (b"iI^I",),
    "MIDIObjectGetStringProperty": (b"iI^{__CFString=}^^{__CFString=}",),
    "MIDIGetExternalDevice": (b"IQ",),
    "MIDIThruConnectionCreate": (
        b"i^{__CFString=}^{__CFData=}^I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"type_modifier": "o"}},
        },
    ),
    "MIDIDeviceListDispose": (b"iI",),
    "MIDISendSysex": (b"i^{MIDISysexSendRequest=I^CIZ[3C]^?^v}",),
    "MIDIGetSerialPortOwner": (
        b"i^{__CFString=}^^{__CFString=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "MIDIGetDevice": (b"IQ",),
    "MIDIThruConnectionSetParams": (b"iI^{__CFData=}",),
    "MIDIDestinationCreateWithProtocol": (
        b"iI^{__CFString=}i^I@?",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MIDIEventListAdd": (
        b"^{MIDIEventPacket=QI[64I]}^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}Q^{MIDIEventPacket=QI[64I]}QQ^I",
    ),
    "MIDIDeviceListGetNumberOfDevices": (b"QI",),
    "MIDIInputPortCreateWithProtocol": (
        b"iI^{__CFString=}i^I@?",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MIDIDeviceGetEntity": (b"IIQ",),
    "MIDIDeviceCreate": (
        b"i^^{MIDIDriverInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?}^{__CFString=}^{__CFString=}^{__CFString=}^I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {4: {"type_modifier": "o"}},
        },
    ),
    "MIDIOutputPortCreate": (
        b"iI^{__CFString=}^I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MIDIEntityGetNumberOfSources": (b"QI",),
    "MIDIEntityGetDestination": (b"IIQ",),
    "MIDIInputPortCreateWithBlock": (
        b"iI^{__CFString=}^I@?",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MIDIGetDriverIORunLoop": (b"^{__CFRunLoop=}",),
    "MIDIReceivedEventList": (b"iI^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}",),
    "MIDIDeviceRemoveEntity": (b"iII",),
    "MIDIGetNumberOfSources": (b"Q",),
    "MIDISourceCreate": (
        b"iI^{__CFString=}^I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MIDISourceCreateWithProtocol": (
        b"iI^{__CFString=}i^I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MIDIEntityGetSource": (b"IIQ",),
}
misc.update(
    {
        "MIDIDriverRef": objc.createOpaquePointerType(
            "MIDIDriverRef", b"^^{MIDriverInterface=}"
        )
    }
)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"MIDICIDiscoveredNode", b"supportsProfiles", {"retval": {"type": b"Z"}})
    r(b"MIDICIDiscoveredNode", b"supportsProperties", {"retval": {"type": b"Z"}})
    r(
        b"MIDICIDiscoveryManager",
        b"discoverWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"MIDICIResponder",
        b"initWithDeviceInfo:profileDelegate:profileStates:supportProperties:",
        {"arguments": {5: {"type": b"Z"}}},
    )
    r(
        b"MIDICIResponder",
        b"notifyProfile:onChannel:isEnabled:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"MIDICIResponder",
        b"sendProfile:onChannel:profileData:",
        {"retval": {"type": b"Z"}},
    )
    r(b"MIDICIResponder", b"start", {"retval": {"type": b"Z"}})
    r(
        b"MIDICISession",
        b"disableProfile:onChannel:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"MIDICISession",
        b"enableProfile:onChannel:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"MIDICISession",
        b"initWithDiscoveredNode:dataReadyHandler:disconnectHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"MIDICISession",
        b"profileChangedCallback",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"q"},
                        3: {"type": b"@"},
                        4: {"type": b"Z"},
                    },
                }
            }
        },
    )
    r(
        b"MIDICISession",
        b"profileSpecificDataHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"q"},
                        3: {"type": b"@"},
                        4: {"type": b"@"},
                    },
                }
            }
        },
    )
    r(
        b"MIDICISession",
        b"sendProfile:onChannel:profileData:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MIDICISession",
        b"setProfileChangedCallback:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"q"},
                            3: {"type": b"@"},
                            4: {"type": b"Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MIDICISession",
        b"setProfileSpecificDataHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"q"},
                            3: {"type": b"@"},
                            4: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"MIDICISession", b"supportsProfileCapability", {"retval": {"type": b"Z"}})
    r(b"MIDICISession", b"supportsPropertyCapability", {"retval": {"type": b"Z"}})
    r(b"MIDINetworkSession", b"addConnection:", {"retval": {"type": "Z"}})
    r(b"MIDINetworkSession", b"addContact:", {"retval": {"type": "Z"}})
    r(b"MIDINetworkSession", b"isEnabled", {"retval": {"type": "Z"}})
    r(b"MIDINetworkSession", b"removeConnection:", {"retval": {"type": "Z"}})
    r(b"MIDINetworkSession", b"removeContact:", {"retval": {"type": "Z"}})
    r(b"MIDINetworkSession", b"setEnabled:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"NSObject",
        b"connectInitiator:withDeviceInfo:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"handleDataForProfile:onChannel:data:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"C"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"initiatorDisconnected:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"willSetProfile:onChannel:enabled:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"C"}, 4: {"type": b"Z"}},
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE