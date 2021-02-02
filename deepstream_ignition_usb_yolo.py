#!/usr/bin/env python3

################################################################################
# Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
################################################################################

import sys
sys.path.append('../')

sys.path.insert(0, "../../../client_libraries/python/")
import paho.mqtt.client as mqtt
import sparkplug_b as sparkplug
import time
import time, threading
import random
import string
import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst
from common.is_aarch_64 import is_aarch64
from common.bus_call import bus_call
from sparkplug_b import *
import pyds

# Application Variables
serverUrl = "localhost"
myGroupId = "Sparkplug B Devices"
myNodeName = "NVIDIA"
myDeviceName = "XavierNX"
publishPeriod = 5000
myUsername = "admin"
myPassword = "changeme"
client = mqtt.Client(serverUrl, 1883, 60)
WAIT_SECONDS = 1
frame_numberx = 0
num_rectsx = 0
counter1 = 0
counter2 = 0

Object1 = 0
Object2 = 0
Object3 = 0
Object4 = 0
Object5 = 0
Object6 = 0
Object7 = 0
Object8 = 0
Object9 = 0
Object10 = 0
newValue1 = 0
newValue2 = 0
newValue3 = 0
newValue4 = 0
newValue5 = 0
newValue6 = 0
newValue7 = 0
newValue8 = 0
newValue9 = 0
newValue10 = 0

class AliasMap:
    Next_Server = 0
    Rebirth = 1
    Reboot = 2
    Device_frame_numberx = 3
    Device_num_rectsx = 4
    Device_Metric0 = 5
    Device_Metric1 = 6
    Device_Metric2 = 7
    Device_Metric3 = 8
    Device_Metric4 = 9
    Device_counter1 = 10
    Device_counter2 = 11   
    Device_Input1 = 12
    Device_Input2 = 13
    Device_Input3 = 14
    Device_Input4 = 15
    Device_Input5 = 16
    Device_Input6 = 17
    Device_Input7 = 18
    Device_Input8 = 19
    Device_Input9 = 20
    Device_Input10 = 21
    Device_Output1 = 22
    Device_Output2 = 23
    Device_Output3 = 24
    Device_Output4 = 25
    Device_Output5 = 26
    Device_Output6 = 27
    Device_Output7 = 28
    Device_Output8 = 29
    Device_Output9 = 30
    Device_Output10 = 31

MAX_DISPLAY_LEN=64
PGIE_CLASS_ID_TOOTHBRUSH = 79
PGIE_CLASS_ID_HAIR_DRYER = 78
PGIE_CLASS_ID_TEDDY_BEAR = 77
PGIE_CLASS_ID_SCISSORS = 76
PGIE_CLASS_ID_VASE = 75
PGIE_CLASS_ID_CLOCK = 74
PGIE_CLASS_ID_BOOK = 73
PGIE_CLASS_ID_REFRIGERATOR = 72
PGIE_CLASS_ID_SINK = 71
PGIE_CLASS_ID_TOASTER = 70
PGIE_CLASS_ID_OVEN = 69
PGIE_CLASS_ID_MICROWAVE = 68
PGIE_CLASS_ID_CELL_PHONE = 67
PGIE_CLASS_ID_KEYBOARD = 66
PGIE_CLASS_ID_REMOTE = 65
PGIE_CLASS_ID_MOUSE = 64
PGIE_CLASS_ID_LAPTOP = 63
PGIE_CLASS_ID_TVMONITOR = 62
PGIE_CLASS_ID_TOILET = 61
PGIE_CLASS_ID_DININGTABLE= 60
PGIE_CLASS_ID_BED = 59
PGIE_CLASS_ID_POTTEDPLANT = 58
PGIE_CLASS_ID_SOFA = 57
PGIE_CLASS_ID_CHAIR = 56
PGIE_CLASS_ID_CAKE = 55
PGIE_CLASS_ID_DONUT = 54
PGIE_CLASS_ID_PIZZA = 53
PGIE_CLASS_ID_HOT_DOG = 52
PGIE_CLASS_ID_CARROT = 51
PGIE_CLASS_ID_BROCCOLI = 50
PGIE_CLASS_ID_ORANGE = 49
PGIE_CLASS_ID_SANDWICH = 48
PGIE_CLASS_ID_APPLE = 47
PGIE_CLASS_ID_BANANA = 46
PGIE_CLASS_ID_BOWL = 45
PGIE_CLASS_ID_SPOON = 44
PGIE_CLASS_ID_KNIFE = 43
PGIE_CLASS_ID_FORK = 42
PGIE_CLASS_ID_CUP = 41
PGIE_CLASS_ID_WINE_GLASS = 40
PGIE_CLASS_ID_BOTTLE = 39
PGIE_CLASS_ID_TENNIS_RACKET = 38
PGIE_CLASS_ID_SURFBOARD = 37
PGIE_CLASS_ID_SKATEBOARD = 36
PGIE_CLASS_ID_BASEBALL_GLOVE = 35
PGIE_CLASS_ID_BASEBALL_BAT = 34
PGIE_CLASS_ID_KITE = 33
PGIE_CLASS_ID_SPORTS_BALL = 32
PGIE_CLASS_ID_SNOWBOARD = 31
PGIE_CLASS_ID_SKIS = 30
PGIE_CLASS_ID_FRISBEE = 29
PGIE_CLASS_ID_SUITCASE = 28
PGIE_CLASS_ID_TIE = 27
PGIE_CLASS_ID_HANDBAG = 26
PGIE_CLASS_ID_UMBRELLA = 25
PGIE_CLASS_ID_BACKPACK = 24
PGIE_CLASS_ID_GIRAFFE = 23
PGIE_CLASS_ID_ZEBRA = 22
PGIE_CLASS_ID_BEAR = 21
PGIE_CLASS_ID_ELEPHANT = 20
PGIE_CLASS_ID_COW = 19
PGIE_CLASS_ID_SHEEP = 18
PGIE_CLASS_ID_HORSE = 17
PGIE_CLASS_ID_DOG = 16
PGIE_CLASS_ID_CAT = 15
PGIE_CLASS_ID_BIRD = 14
PGIE_CLASS_ID_BENCH = 13
PGIE_CLASS_ID_PARKING_METER = 12
PGIE_CLASS_ID_STOP_SIGN = 11
PGIE_CLASS_ID_FIRE_HYDRANT = 10
PGIE_CLASS_ID_TRAFFIC_LIGHT = 9
PGIE_CLASS_ID_BOAT = 8
PGIE_CLASS_ID_TRUCK = 7
PGIE_CLASS_ID_TRAIN = 6
PGIE_CLASS_ID_BUS = 5
PGIE_CLASS_ID_AEROPLANE = 4
PGIE_CLASS_ID_MOTORBIKE = 3
PGIE_CLASS_ID_VEHICLE = 2
PGIE_CLASS_ID_BICYCLE = 1
PGIE_CLASS_ID_PERSON = 0

pgie_classes_str= ["Toothbrush", "Hair dryer", "Teddy bear","Scissors","Vase", "Clock", "Book","Refrigerator", "Sink", "Toaster","Oven","Microwave", "Cell phone", "Keyboard","Remote", "Mouse", "Laptop","Tvmonitor","Toilet", "Diningtable", "Bed","Pottedplant", "Sofa", "Chair","Cake","Donut", "Pizza", "Hot dog","Carrot", "Broccli", "Orange","Sandwich","Apple", "Banana", "Bowl","Spoon", "Knife", "Fork","Cup","Wine Glass", "Bottle", "Tennis racket","Surfboard", "Skateboard", "Baseball glove","Baseball bat","Kite", "Sports ball", "Snowboard","Skis", "Frisbee", "Suitcase","Tie","Handbag", "Umbrella", "Backpack","Giraffe", "Zebra", "Bear","Elephant","Cow", "Sheep", "Horse","Dog", "Cat", "Bird","Bench","Parking meter", "Stop sign", "Fire hydrant","Traffic light", "Boat", "Truck","Train","Bus", "Areoplane", "Motorbike","Car", "Bicycle", "Person"]

######################################################################
# The callback for when the client receives a CONNACK response from the server.
######################################################################
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with result code "+str(rc))
    else:
        print("Failed to connect with result code "+str(rc))
        sys.exit()

    global myGroupId
    global myNodeName

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("spBv1.0/" + myGroupId + "/NCMD/" + myNodeName + "/#")
    client.subscribe("spBv1.0/" + myGroupId + "/DCMD/" + myNodeName + "/#")
######################################################################

######################################################################
# The callback for when a PUBLISH message is received from the server.
######################################################################
def on_message(client, userdata, msg):
    print("Message arrived: " + msg.topic)
    tokens = msg.topic.split("/")
    global newValue1
    global newValue2
    global newValue3
    global newValue4
    global newValue5
    global newValue6
    global newValue7
    global newValue8
    global newValue9
    global newValue10
    if tokens[0] == "spBv1.0" and tokens[1] == myGroupId and (tokens[2] == "NCMD" or tokens[2] == "DCMD") and tokens[3] == myNodeName:
        inboundPayload = sparkplug_b_pb2.Payload()
        inboundPayload.ParseFromString(msg.payload)
        for metric in inboundPayload.metrics:
            if metric.name == "Node Control/Next Server" or metric.alias == AliasMap.Next_Server:
                # 'Node Control/Next Server' is an NCMD used to tell the device/client application to
                # disconnect from the current MQTT server and connect to the next MQTT server in the
                # list of available servers.  This is used for clients that have a pool of MQTT servers
                # to connect to.
                print ("'Node Control/Next Server' is not implemented in this example")
            elif metric.name == "Node Control/Rebirth" or metric.alias == AliasMap.Rebirth:
                # 'Node Control/Rebirth' is an NCMD used to tell the device/client application to resend
                # its full NBIRTH and DBIRTH again.  MQTT Engine will send this NCMD to a device/client
                # application if it receives an NDATA or DDATA with a metric that was not published in the
                # original NBIRTH or DBIRTH.  This is why the application must send all known metrics in
                # its original NBIRTH and DBIRTH messages.
                publishBirth()
            elif metric.name == "Node Control/Reboot" or metric.alias == AliasMap.Reboot:
                # 'Node Control/Reboot' is an NCMD used to tell a device/client application to reboot
                # This can be used for devices that need a full application reset via a soft reboot.
                # In this case, we fake a full reboot with a republishing of the NBIRTH and DBIRTH
                # messages.
                publishBirth()
            elif metric.name == "output/Device Metric2" or metric.alias == AliasMap.Device_Metric2:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue = metric.int_value
                print ("CMD message for output/Device Metric2 - New Value: {}".format(newValue))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Metric2, MetricDataType.Int16, newValue)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)

               # Publish a message Input 1
                #publishBirth()
            elif metric.name == "output/Device Input1" or metric.alias == AliasMap.Device_Input1:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue1 = metric.int_value
                print ("CMD message for output/Device Input1 - New Value: {}".format(newValue1))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input1, MetricDataType.Int16, newValue1)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)
          
                # Publish a message Input 2
                #publishBirth()
            elif metric.name == "output/Device Input2" or metric.alias == AliasMap.Device_Input2:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue2 = metric.int_value
                print ("CMD message for output/Device Input2 - New Value: {}".format(newValue2))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input2, MetricDataType.Int16, newValue2)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False) 
 
               # Publish a message Input 3
               #publishBirth()
            elif metric.name == "output/Device Input3" or metric.alias == AliasMap.Device_Input3:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue3 = metric.int_value
                print ("CMD message for output/Device Input3 - New Value: {}".format(newValue3))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input3, MetricDataType.Int16, newValue3)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)
                 
                # Publish a message Input 4
                #publishBirth()
            elif metric.name == "output/Device Input4" or metric.alias == AliasMap.Device_Input4:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue4 = metric.int_value
                print ("CMD message for output/Device Input4 - New Value: {}".format(newValue4))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input4, MetricDataType.Int16, newValue4)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)
 
               # Publish a message Input 5
                #publishBirth()
            elif metric.name == "output/Device Input5" or metric.alias == AliasMap.Device_Input5:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue5 = metric.int_value
                print ("CMD message for output/Device Input5 - New Value: {}".format(newValue5))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input5, MetricDataType.Int16, newValue5)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False) 

                # Publish a message Input 6
                #publishBirth()
            elif metric.name == "output/Device Input6" or metric.alias == AliasMap.Device_Input6:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue6 = metric.int_value
                print ("CMD message for output/Device Input6 - New Value: {}".format(newValue6))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input6, MetricDataType.Int16, newValue6)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False) 

                # Publish a message Input 7
                #publishBirth()
            elif metric.name == "output/Device Input7" or metric.alias == AliasMap.Device_Input7:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue7 = metric.int_value
                print ("CMD message for output/Device Input7 - New Value: {}".format(newValue7))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input7, MetricDataType.Int16, newValue7)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)

                # Publish a message Input 8
                #publishBirth()
            elif metric.name == "output/Device Input8" or metric.alias == AliasMap.Device_Input8:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue8 = metric.int_value
                print ("CMD message for output/Device Input8 - New Value: {}".format(newValue8))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input8, MetricDataType.Int16, newValue8)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False) 

                # Publish a message Input 9
                 #publishBirth()
            elif metric.name == "output/Device Input9" or metric.alias == AliasMap.Device_Input9:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue9 = metric.int_value
                print ("CMD message for output/Device Input9 - New Value: {}".format(newValue9))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input9, MetricDataType.Int16, newValue9)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False) 

                # Publish a message Input 10
                 #publishBirth()
            elif metric.name == "output/Device Input10" or metric.alias == AliasMap.Device_Input10:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue10 = metric.int_value
                print ("CMD message for output/Device Input10 - New Value: {}".format(newValue10))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Input10, MetricDataType.Int16, newValue10)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)   

                #global newValue4     
                 #publishBirth()
            elif metric.name == "output/Device Metric4" or metric.alias == AliasMap.Device_Metric4:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Int16 because of how we declated it in the DBIRTH
                newValue = metric.string_value
                
                print ("CMD message for output/Device Metric4 - New Value: {}".format(newValue))

                # Create the DDATA payload - Use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Metric4, MetricDataType.String, newValue)
                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)

                #publishBirth()
            elif metric.name == "output/Device Metric3" or metric.alias == AliasMap.Device_Metric3:
                # This is a metric we declared in our DBIRTH message and we're emulating an output.
                # So, on incoming 'writes' to the output we must publish a DDATA with the new output
                # value.  If this were a real output we'd write to the output and then read it back
                # before publishing a DDATA message.

                # We know this is an Boolean because of how we declated it in the DBIRTH
                newValue = metric.boolean_value
                print ("CMD message for output/Device Metric3 - New Value: %r" % newValue)

                # Create the DDATA payload - use the alias because this isn't the DBIRTH
                payload = sparkplug.getDdataPayload()
                addMetric(payload, None, AliasMap.Device_Metric3, MetricDataType.Boolean, newValue)

                # Publish a message data
                byteArray = bytearray(payload.SerializeToString())
                client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)
            else:
                print ("Unknown command: " + metric.name)
    else:
        print ("Unknown command...")

    print ("Done publishing")
#####################################################################
######################################################################

######################################################################
# Publish the BIRTH certificates
######################################################################
def publishBirth():
    publishNodeBirth()
    publishDeviceBirth()
######################################################################

######################################################################
# Publish the NBIRTH certificate
######################################################################
def publishNodeBirth():
    print ("Publishing Node Birth")

    # Create the node birth payload
    payload = sparkplug.getNodeBirthPayload()

    # Set up the Node Controls
    addMetric(payload, "Node Control/Next Server", AliasMap.Next_Server, MetricDataType.Boolean, False)
    addMetric(payload, "Node Control/Rebirth", AliasMap.Rebirth, MetricDataType.Boolean, False)
    addMetric(payload, "Node Control/Reboot", AliasMap.Reboot, MetricDataType.Boolean, False)

    # Publish the node birth certificate
    byteArray = bytearray(payload.SerializeToString())
    client.publish("spBv1.0/" + myGroupId + "/NBIRTH/" + myNodeName, byteArray, 0, False)

######################################################################

######################################################################
# Publish the DBIRTH certificate
######################################################################
def publishDeviceBirth():
    print ("Publishing Device Birth")

    # Get the payload
    payload = sparkplug.getDeviceBirthPayload()
    
    # Add some device metrics
    addMetric(payload, "input/Frame Number", AliasMap.Device_frame_numberx, MetricDataType.Int16, frame_numberx )
    addMetric(payload, "input/Device Metric0", AliasMap.Device_Metric0, MetricDataType.String, "hello device")
    addMetric(payload, "input/Device Metric1", AliasMap.Device_Metric1, MetricDataType.Boolean, True)
    addMetric(payload, "input/Number of Objects", AliasMap.Device_num_rectsx, MetricDataType.Int16, num_rectsx )
    addMetric(payload, "output/Device Metric2", AliasMap.Device_Metric2, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input1", AliasMap.Device_Input1, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input2", AliasMap.Device_Input2, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input3", AliasMap.Device_Input3, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input4", AliasMap.Device_Input4, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input5", AliasMap.Device_Input5, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input6", AliasMap.Device_Input6, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input7", AliasMap.Device_Input7, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input8", AliasMap.Device_Input8, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input9", AliasMap.Device_Input9, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Input10", AliasMap.Device_Input10, MetricDataType.Int16, 0)
    addMetric(payload,"input/Device Output1", AliasMap.Device_Output1, MetricDataType.Int16, 0)
    addMetric(payload, "input/Device Output2", AliasMap.Device_Output2, MetricDataType.Int16, 0)
    addMetric(payload, "input/Device Output3", AliasMap.Device_Output3, MetricDataType.Int16, 0)
    addMetric(payload, "input/Device Output4", AliasMap.Device_Output4, MetricDataType.Int16, 0)
    addMetric(payload, "input/Device Output5", AliasMap.Device_Output5, MetricDataType.Int16, 0)
    addMetric(payload, "input/Device Output6", AliasMap.Device_Output6, MetricDataType.Int16, 0)
    addMetric(payload, "input/Device Output7", AliasMap.Device_Output7, MetricDataType.Int16, 0)
    addMetric(payload, "input/Device Output8", AliasMap.Device_Output8, MetricDataType.Int16, 0)
    addMetric(payload, "input/Device Output9", AliasMap.Device_Output9, MetricDataType.Int16, 0)
    addMetric(payload, "input/Device Output10", AliasMap.Device_Output10, MetricDataType.Int16, 0)
    addMetric(payload, "output/Device Metric3", AliasMap.Device_Metric3, MetricDataType.Boolean, True)
    addMetric(payload, "output/Device Metric4", AliasMap.Device_Metric4, MetricDataType.String, "start")

    # Publish the initial data with the Device BIRTH certificate
    totalByteArray = bytearray(payload.SerializeToString())
    client.publish("spBv1.0/" + myGroupId + "/DBIRTH/" + myNodeName + "/" + myDeviceName, totalByteArray, 0, False)
######################################################################

######################################################################
    

def osd_sink_pad_buffer_probe(pad,info,u_data):
    global frame_numberx
    global num_rectsx
    global Object1
    global Object2
    global Object3
    global Object4
    global Object5
    global Object6
    global Object7
    global Object8
    global Object9
    global Object10
    
   
    #Intiallizing object counter with 0.
    obj_counter = {
        PGIE_CLASS_ID_TOOTHBRUSH:0,
        PGIE_CLASS_ID_HAIR_DRYER:0,
        PGIE_CLASS_ID_TEDDY_BEAR:0,
        PGIE_CLASS_ID_SCISSORS:0,
        PGIE_CLASS_ID_VASE:0,
        PGIE_CLASS_ID_CLOCK:0,
        PGIE_CLASS_ID_BOOK:0,
        PGIE_CLASS_ID_REFRIGERATOR:0,
        PGIE_CLASS_ID_SINK:0,
        PGIE_CLASS_ID_TOASTER:0,
        PGIE_CLASS_ID_OVEN:0,
        PGIE_CLASS_ID_MICROWAVE:0,
        PGIE_CLASS_ID_CELL_PHONE:0,
        PGIE_CLASS_ID_KEYBOARD:0,
        PGIE_CLASS_ID_REMOTE:0,
        PGIE_CLASS_ID_MOUSE:0,
        PGIE_CLASS_ID_LAPTOP:0,
        PGIE_CLASS_ID_TVMONITOR:0,
        PGIE_CLASS_ID_TOILET:0,
        PGIE_CLASS_ID_DININGTABLE:0,
        PGIE_CLASS_ID_BED:0,
        PGIE_CLASS_ID_POTTEDPLANT:0,
        PGIE_CLASS_ID_SOFA:0,
        PGIE_CLASS_ID_CHAIR:0,
        PGIE_CLASS_ID_CAKE:0,
        PGIE_CLASS_ID_DONUT:0,
        PGIE_CLASS_ID_PIZZA:0,
        PGIE_CLASS_ID_HOT_DOG:0,
        PGIE_CLASS_ID_CARROT:0,
        PGIE_CLASS_ID_BROCCOLI:0,
        PGIE_CLASS_ID_ORANGE:0,
        PGIE_CLASS_ID_SANDWICH:0,
        PGIE_CLASS_ID_APPLE:0,
        PGIE_CLASS_ID_BANANA:0,
        PGIE_CLASS_ID_BOWL:0,
        PGIE_CLASS_ID_SPOON:0,
        PGIE_CLASS_ID_KNIFE:0,
        PGIE_CLASS_ID_FORK:0,
        PGIE_CLASS_ID_CUP:0,
        PGIE_CLASS_ID_WINE_GLASS:0,
        PGIE_CLASS_ID_BOTTLE:0,
        PGIE_CLASS_ID_TENNIS_RACKET:0,
        PGIE_CLASS_ID_SURFBOARD:0,
        PGIE_CLASS_ID_SKATEBOARD:0,
        PGIE_CLASS_ID_BASEBALL_GLOVE:0,
        PGIE_CLASS_ID_BASEBALL_BAT:0,
        PGIE_CLASS_ID_KITE:0,
        PGIE_CLASS_ID_SPORTS_BALL:0,
        PGIE_CLASS_ID_SNOWBOARD:0,
        PGIE_CLASS_ID_SKIS:0,
        PGIE_CLASS_ID_FRISBEE:0,
        PGIE_CLASS_ID_SUITCASE:0,
        PGIE_CLASS_ID_TIE:0,
        PGIE_CLASS_ID_HANDBAG:0,
        PGIE_CLASS_ID_UMBRELLA:0,
        PGIE_CLASS_ID_BACKPACK:0,
        PGIE_CLASS_ID_GIRAFFE:0,
        PGIE_CLASS_ID_ZEBRA:0,
        PGIE_CLASS_ID_BEAR:0,
        PGIE_CLASS_ID_ELEPHANT:0,
        PGIE_CLASS_ID_COW:0,
        PGIE_CLASS_ID_SHEEP:0,
        PGIE_CLASS_ID_HORSE:0,
        PGIE_CLASS_ID_DOG:0,
        PGIE_CLASS_ID_CAT:0,
        PGIE_CLASS_ID_BIRD:0,
        PGIE_CLASS_ID_BENCH:0,
        PGIE_CLASS_ID_PARKING_METER:0,
        PGIE_CLASS_ID_STOP_SIGN:0,
        PGIE_CLASS_ID_FIRE_HYDRANT:0,
        PGIE_CLASS_ID_TRAFFIC_LIGHT:0,
        PGIE_CLASS_ID_BOAT:0,
        PGIE_CLASS_ID_TRUCK:0,
        PGIE_CLASS_ID_TRAIN:0,
        PGIE_CLASS_ID_BUS:0,
        PGIE_CLASS_ID_AEROPLANE:0,
        PGIE_CLASS_ID_MOTORBIKE:0,
        PGIE_CLASS_ID_VEHICLE:0,
        PGIE_CLASS_ID_BICYCLE:0,
        PGIE_CLASS_ID_PERSON:0
        }
    num_rects=0

    gst_buffer = info.get_buffer()
    if not gst_buffer:
        print("Unable to get GstBuffer ")
        return

    # Retrieve batch metadata from the gst_buffer
    # Note that pyds.gst_buffer_get_nvds_batch_meta() expects the
    # C address of gst_buffer as input, which is obtained with hash(gst_buffer)
    batch_meta = pyds.gst_buffer_get_nvds_batch_meta(hash(gst_buffer))
    l_frame = batch_meta.frame_meta_list
    
    while l_frame is not None:
        try:
            # Note that l_frame.data needs a cast to pyds.NvDsFrameMeta
            # The casting is done by pyds.NvDsFrameMeta.cast()
            # The casting also keeps ownership of the underlying memory
            # in the C code, so the Python garbage collector will leave
            # it alone.
           frame_meta = pyds.NvDsFrameMeta.cast(l_frame.data)
        except StopIteration:
            break

        frame_number=frame_meta.frame_num
        frame_numberx=frame_meta.frame_num
        num_rects = frame_meta.num_obj_meta
        num_rectsx = frame_meta.num_obj_meta
        l_obj=frame_meta.obj_meta_list
        while l_obj is not None:
            try:
                # Casting l_obj.data to pyds.NvDsObjectMeta
                obj_meta=pyds.NvDsObjectMeta.cast(l_obj.data)
            except StopIteration:
                break
            obj_counter[obj_meta.class_id] += 1
            try: 
                l_obj=l_obj.next
            except StopIteration:
                break

        # Acquiring a display meta object. The memory ownership remains in
        # the C code so downstream plugins can still access it. Otherwise
        # the garbage collector will claim it when this probe function exits.
        display_meta=pyds.nvds_acquire_display_meta_from_pool(batch_meta)
        display_meta.num_labels = 1
        py_nvosd_text_params = display_meta.text_params[0]
        # Setting display text to be shown on screen
        # Note that the pyds module allocates a buffer for the string, and the
        # memory will not be claimed by the garbage collector.
        # Reading the display_text field here will return the C address of the
        # allocated string. Use pyds.get_string() to get the string content.
        py_nvosd_text_params.display_text = "Frame Number={} Number of Objects={} Bird_count={} Person_count={}".format(frame_number, num_rects, obj_counter[PGIE_CLASS_ID_CUP], obj_counter[PGIE_CLASS_ID_BOTTLE])

        Object1 = obj_counter[newValue1]
        Object2 = obj_counter[newValue2]
        Object3 = obj_counter[newValue3]
        Object4 = obj_counter[newValue4]
        Object5 = obj_counter[newValue5]
        Object6 = obj_counter[newValue6]
        Object7 = obj_counter[newValue7]
        Object8 = obj_counter[newValue8]
        Object9 = obj_counter[newValue9]
        Object10 = obj_counter[newValue10]
        
        # Now set the offsets where the string should appear
        py_nvosd_text_params.x_offset = 10
        py_nvosd_text_params.y_offset = 12
    
        # Font , font-color and font-size
        py_nvosd_text_params.font_params.font_name = "Serif"
        py_nvosd_text_params.font_params.font_size = 10
        # set(red, green, blue, alpha); set to White
        py_nvosd_text_params.font_params.font_color.set(1.0, 1.0, 1.0, 1.0)

        # Text background color
        py_nvosd_text_params.set_bg_clr = 1
        # set(red, green, blue, alpha); set to Black
        py_nvosd_text_params.text_bg_clr.set(0.0, 0.0, 0.0, 1.0)
        # Using pyds.get_string() to get display_text as string
       # print(pyds.get_string(py_nvosd_text_params.display_text))
        #pyds.nvds_add_display_meta_to_frame(frame_meta, display_meta)
        try:
            l_frame=l_frame.next
        except StopIteration:
            break
			
    return Gst.PadProbeReturn.OK	
    ######################################################################


def main(args):
    
    # Check input arguments
    if len(args) != 2:
        sys.stderr.write("usage: %s <v4l2-device-path>\n" % args[0])
        sys.exit(1)

    # Standard GStreamer initialization
    GObject.threads_init()
    Gst.init(None)
    
    # Create gstreamer elements
    # Create Pipeline element that will form a connection of other elements
    print("Creating Pipeline \n ")
    pipeline = Gst.Pipeline()
    if not pipeline:
        sys.stderr.write(" Unable to create Pipeline \n")

    # Source element for reading from the file
    print("Creating Source \n ")
    source = Gst.ElementFactory.make("v4l2src", "usb-cam-source")
    if not source:
        sys.stderr.write(" Unable to create Source \n")

    caps_v4l2src = Gst.ElementFactory.make("capsfilter", "v4l2src_caps")
    if not caps_v4l2src:
        sys.stderr.write(" Unable to create v4l2src capsfilter \n")


    print("Creating Video Converter \n")

    # Adding videoconvert -> nvvideoconvert as not all
    # raw formats are supported by nvvideoconvert;
    # Say YUYV is unsupported - which is the common
    # raw format for many logi usb cams
    # In case we have a camera with raw format supported in
    # nvvideoconvert, GStreamer plugins' capability negotiation
    # shall be intelligent enough to reduce compute by
    # videoconvert doing passthrough (TODO we need to confirm this)


    # videoconvert to make sure a superset of raw formats are supported
    vidconvsrc = Gst.ElementFactory.make("videoconvert", "convertor_src1")
    if not vidconvsrc:
        sys.stderr.write(" Unable to create videoconvert \n")

    # nvvideoconvert to convert incoming raw buffers to NVMM Mem (NvBufSurface API)
    nvvidconvsrc = Gst.ElementFactory.make("nvvideoconvert", "convertor_src2")
    if not nvvidconvsrc:
        sys.stderr.write(" Unable to create Nvvideoconvert \n")

    caps_vidconvsrc = Gst.ElementFactory.make("capsfilter", "nvmm_caps")
    if not caps_vidconvsrc:
        sys.stderr.write(" Unable to create capsfilter \n")

    # Create nvstreammux instance to form batches from one or more sources.
    streammux = Gst.ElementFactory.make("nvstreammux", "Stream-muxer")
    if not streammux:
        sys.stderr.write(" Unable to create NvStreamMux \n")

    # Use nvinfer to run inferencing on camera's output,
    # behaviour of inferencing is set through config file
    pgie = Gst.ElementFactory.make("nvinfer", "primary-inference")
    if not pgie:
        sys.stderr.write(" Unable to create pgie \n")

    # Use convertor to convert from NV12 to RGBA as required by nvosd
    nvvidconv = Gst.ElementFactory.make("nvvideoconvert", "convertor")
    if not nvvidconv:
        sys.stderr.write(" Unable to create nvvidconv \n")

    # Create OSD to draw on the converted RGBA buffer
    nvosd = Gst.ElementFactory.make("nvdsosd", "onscreendisplay")

    if not nvosd:
        sys.stderr.write(" Unable to create nvosd \n")

    # Finally render the osd output
    if is_aarch64():
        transform = Gst.ElementFactory.make("nvegltransform", "nvegl-transform")

    print("Creating EGLSink \n")
    sink = Gst.ElementFactory.make("nveglglessink", "nvvideo-renderer")
    if not sink:
        sys.stderr.write(" Unable to create egl sink \n")

    print("Playing cam %s " %args[1])
    caps_v4l2src.set_property('caps', Gst.Caps.from_string("video/x-raw, framerate=30/1"))
    caps_vidconvsrc.set_property('caps', Gst.Caps.from_string("video/x-raw(memory:NVMM)"))
    source.set_property('device', args[1])
    streammux.set_property('width', 640)
    streammux.set_property('height', 480)
    streammux.set_property('batch-size', 1)
    streammux.set_property('batched-push-timeout', 4000000)
    pgie.set_property('config-file-path', "config_infer_primary_yoloV3.txt")
    # Set sync = false to avoid late frame drops at the display-sink
    sink.set_property('sync', False)

    print("Adding elements to Pipeline \n")
    pipeline.add(source)
    pipeline.add(caps_v4l2src)
    pipeline.add(vidconvsrc)
    pipeline.add(nvvidconvsrc)
    pipeline.add(caps_vidconvsrc)
    pipeline.add(streammux)
    pipeline.add(pgie)
    pipeline.add(nvvidconv)
    pipeline.add(nvosd)
    pipeline.add(sink)
    if is_aarch64():
        pipeline.add(transform)

    # we link the elements together
    # v4l2src -> nvvideoconvert -> mux -> 
    # nvinfer -> nvvideoconvert -> nvosd -> video-renderer
    print("Linking elements in the Pipeline \n")
    source.link(caps_v4l2src)
    caps_v4l2src.link(vidconvsrc)
    vidconvsrc.link(nvvidconvsrc)
    nvvidconvsrc.link(caps_vidconvsrc)

    sinkpad = streammux.get_request_pad("sink_0")
    if not sinkpad:
        sys.stderr.write(" Unable to get the sink pad of streammux \n")
    srcpad = caps_vidconvsrc.get_static_pad("src")
    if not srcpad:
        sys.stderr.write(" Unable to get source pad of caps_vidconvsrc \n")
    srcpad.link(sinkpad)
    streammux.link(pgie)
    pgie.link(nvvidconv)
    nvvidconv.link(nvosd)
    if is_aarch64():
        nvosd.link(transform)
        transform.link(sink)
    else:
        nvosd.link(sink)

    # create an event loop and feed gstreamer bus mesages to it
    loop = GObject.MainLoop()
    bus = pipeline.get_bus()
    bus.add_signal_watch()
    bus.connect ("message", bus_call, loop)

    # Lets add probe to get informed of the meta data generated, we add probe to
    # the sink pad of the osd element, since by that time, the buffer would have
    # had got all the metadata.
    osdsinkpad = nvosd.get_static_pad("sink")
    if not osdsinkpad:
        sys.stderr.write(" Unable to get sink pad of nvosd \n")
    osdsinkpad.add_probe(Gst.PadProbeType.BUFFER, osd_sink_pad_buffer_probe, 0)
    
######################################################################
    # Create the node death payload
    deathPayload = sparkplug.getNodeDeathPayload()

    # Start of main program - Set up the MQTT client connection
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(myUsername, myPassword)
    deathByteArray = bytearray(deathPayload.SerializeToString())
    client.will_set("spBv1.0/" + myGroupId + "/NDEATH/" + myNodeName, deathByteArray, 0, False)
    client.connect(serverUrl, 1883, 60)

    # Publish the birth certificates
    publishBirth()
    
    def foo():

        # Periodically publish some new data
        payload = sparkplug.getDdataPayload()

          # Add some random data to the inputs
        addMetric(payload, "input/number of objects", AliasMap.Device_num_rectsx, MetricDataType.Int16, num_rectsx )
        addMetric(payload, "input/Frame Number", AliasMap.Device_frame_numberx, MetricDataType.Int16, frame_numberx )
        addMetric(payload,"input/Device Output1", AliasMap.Device_Output1, MetricDataType.Int16, Object1)
        addMetric(payload, "input/Device Output2", AliasMap.Device_Output2, MetricDataType.Int16, Object2)
        addMetric(payload, "input/Device Output3", AliasMap.Device_Output3, MetricDataType.Int16, Object3)
        addMetric(payload, "input/Device Output4", AliasMap.Device_Output4, MetricDataType.Int16, Object4)
        addMetric(payload, "input/Device Output5", AliasMap.Device_Output5, MetricDataType.Int16, Object5)
        addMetric(payload, "input/Device Output6", AliasMap.Device_Output6, MetricDataType.Int16, Object6)
        addMetric(payload, "input/Device Output7", AliasMap.Device_Output7, MetricDataType.Int16, Object7)
        addMetric(payload, "input/Device Output8", AliasMap.Device_Output8, MetricDataType.Int16, Object8)
        addMetric(payload, "input/Device Output9", AliasMap.Device_Output9, MetricDataType.Int16, Object9)
        addMetric(payload, "input/Device Output10", AliasMap.Device_Output10, MetricDataType.Int16, Object10)

        # Publish a message data
        byteArray = bytearray(payload.SerializeToString())
        client.publish("spBv1.0/" + myGroupId + "/DDATA/" + myNodeName + "/" + myDeviceName, byteArray, 0, False)

        # Sit and wait for inbound or outbound events
        for _ in range(1):
              time.sleep(1)
              client.loop()
        threading.Timer(WAIT_SECONDS, foo).start()

    foo()     
######################################################################
    print("Starting pipeline \n")
    pipeline.set_state(Gst.State.PLAYING)
    try:
      loop.run()
    except:
        pass
     #cleanup
    print("Exiting app\n")
    pipeline.set_state(Gst.State.NULL)
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))


