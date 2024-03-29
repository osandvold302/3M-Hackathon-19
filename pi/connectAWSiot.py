from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import RPi.GPIO as GPIO
import logging
import time
import argparse
import json

# set up Pi pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# AWS
host =  # retrieve endpoint from IOTCORE/Settings #"a15llkyp1ib6yl-ats.iot.us-east-1.amazonaws.com"
certPath = "/home/pi/certificates/" # key, certificate, aws root cert
clientId = "osandvold"
topic = "online-post-it"    # iot topic 

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, 8883)
myAWSIoTMQTTClient.configureCredentials("{}aws-root-cert.pem".format(certPath), "{}private-key.pem.key".format(certPath), "{}iot-cert.pem.crt".format(certPath))

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myAWSIoTMQTTClient.connect()

while True:
    message = {}
    input_state = GPIO.input(18)
    if input_state == GPIO.HIGH:
        message['message'] = "Dash Button Pressed in Room 201 C"
        messageJson = json.dumps(message)
        myAWSIoTMQTTClient.publish(topic, messageJson, 1)
        print('Published topic %s: %s\n' % (topic, messageJson))
        time.sleep(15)  # TODO: Set to 60 for real example

myAWSIoTMQTTClient.disconnect()