import paho.mqtt.client as mqtt
import ssl
import json,time
import RPi.GPIO as GPIO
 

GPIO.setwarnings(True) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

for i in range(0,5):
    print GPIO.input(4)
  
#Connection credentials to AWS IoT
client = mqtt.Client(client_id="coffeeMate")
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(ca_certs='/home/pi/root-CA.pem', certfile='/home/pi/xxxxx-certificate.pem.crt', keyfile='/home/pi/xxxxx-private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("xxxxx.iot.us-west-2.amazonaws.com", 8883, 30)
client.loop_forever()
