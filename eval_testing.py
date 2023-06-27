import random
import time
import sys
from Adafruit_IO import MQTTClient
import requests

AIO_FEED_ID = ["button1","button2","equation"]
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




global_equation = "x1 + x2 +x3  "
def init_global_equation():
    headers = {}
    aio_url= "https://io.adafruit.com/api/v2/NhanVGU/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()
    global_equation = data["last_value"]

    print("Get lastest value :", global_equation)


def modify_value(x1,x2,x3) :
    result = eval(global_equation)
    return result


def connected(client) :
    print("sever connected...")
    client.subscribe("button1")
    client.subscribe("button2")
    client.subscribe("equation")


def message(client, feed_id, payload) :

    print(f"received: payload from {feed_id} : {payload}" )
    if(feed_id == "equation") :
        global_equation = payload
        print(global_equation)


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
init_global_equation()

while True:

    value = random.randint(0,1)
    value2 = random.randint(1,10)
    value3 = random.randint(1, 10)
    value4 = random.randint(1, 10)
    client.publish("button1", value)
    client.publish("button2", value)
    print(f"value of equation is {value2} {value3} {value4}")
    result1 = modify_value(value2,value3,value4 )
    print("my result is : ", result1)
    time.sleep(10)
    pass


