
import random
import time
import sys
from Adafruit_IO import MQTTClient
#from Basic_AI import *
from datetime import date, datetime
from Hardware import *
import sys
import requests
AIO_FEED_ID = ["Time","Today","Humidity","Temperature","Button"]
AIO_USERNAME = "NhanVGU"
AIO_KEY = "aio_aknu86dhntoRNyBIt7dtooolcs6T"

def connected(client):
    print("Connected to server!!!")
    for things in AIO_FEED_ID:
        client.subscribe(things)




def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe sucessfully ...")
def disconnected(client):
    print("Disconnected ...")
    sys.exit (1)
"""global_equation = "x1 + x2 +x3  "

def init_global_equation():
    headers = {}
    aio_url= "https://io.adafruit.com/api/v2/NhanVGU/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()
    global_equation = data["last_value"]

def modify_value(x1,x2,x3) :
    result = eval(global_equation)
    return result"""

def message(client , feed_id , payload):
    print(f"AI result from {feed_id } : {payload}")
    if feed_id == "Button" :
        values.append(payload)
        write_to_file(values, "data.txt")
    """if(feed_id == "equation") :
        global_equation = payload
        print(global_equation)"""
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
#pre_ai_result =""
#ai_results =""

turn_on = turn_on_AC()
client.publish("Button", turn_on)
check = 1
values = [1]
write_to_file(values, "data.txt")
while True:


        #pre_ai_result = ai_results
        #ai_cap = AI_Identifying()
        #if pre_ai_result != ai_results :
        humi = humidity()
        tem = temperature()
        now = datetime.now()
        today = date.today()
        client.publish("Time", now.strftime("%H hours %M minutes %S seconds"))
        #client.publish("Mask_AI",ai_results)
        #client.publish("General_Vision",ai_cap)
        client.publish("Today", today.strftime("%B %d, %Y"))
        client.publish("Humidity", humi)
        client.publish("Temperature",tem)
        if tem <= 20  :

            if check != 0  :
                client.publish("Button", 0)


                check = 0
        if tem > 20 :

            if check  != 1  :
                client.publish("Button", 1)


                check = 1
        time.sleep(10)
        """keyboard_input = cv2.waitKey(1)
        if keyboard_input == 27:
            break"""