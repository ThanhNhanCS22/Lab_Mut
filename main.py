import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ["sensor1","sensor2", "sensor3"]
AIO_USERNAME = "NhanVGU"
AIO_KEY = ""

def connected(client):
    print("Connected to server!!!")
    for things in AIO_FEED_ID:
        client.subscribe(things)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    value = random.randint(0, 100)
    client.publish("sensor1", value)
    client.publish("sensor2", value)
    client.publish("sensor3", value)
    time.sleep(5)
