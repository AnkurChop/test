import paho.mqtt.client as mqtt
import time

client = mqtt.Client()

client_id="chopsy" 

# Define event callbacks

def on_connect(client, userdata, rc):
    if rc == 0:
         print("Connected successfully.")
    else:
         print("Connection failed. rc= "+str(rc))

def on_publish(client, userdata, mid):
    print("Message "+str(mid)+" published.")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mid "+str(mid)+" received.")

def on_message(client, userdata, msg):
    print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+msg.payload)

mqttclient = mqtt.Client()
print("a")
moisture_set = ["32.5", "29.4", "28.6", "26.5", "24.4", "24.2", "22.9", "30.4", "39.3", "41.6", "40.5", "39.4", "38.6", "36.5", "34.4", "34.2", "32.9", "30.4", "29.3", "21.6","32.4", "37.3", "43.6"]
temp_set=["30.2", "30.1","30.4","31.2","30.7", "30.7", "30.9", "31.6", "29.7", "30.5","32.2","31.7", "30.7", "29.9", "31.8", "29.7","31.2","30.7", "30.7", "30.9", "31.6", "29.7", "30.5"]
wat_lvl_set=["460.5", "460.5", "460.5", "460.5", "460.5", "460.5", "460.5", "394.6", "347.5", "299.2", "299.2", "299.2", "299.2", "299.2","299.2","299.2","299.2","299.2","299.2","299.2","232.2","206.7","188.9"]

# Assign event callbacks
mqttclient.on_connect = on_connect
mqttclient.on_publish = on_publish
mqttclient.on_subscribe = on_subscribe
mqttclient.on_message = on_message

# Connect
mqttclient.username_pw_set("ankursharingan@gmail.com", "8ebfe18f")
mqttclient.connect("mqtt.dioty.co", 1883)

# Start subscription
mqttclient.subscribe("/ankursharingan@gmail.com/")

# Publish a message

'''mqttclient.publish("/ankursharingan@gmail.com/test1", "34" )
time.sleep(3)
mqttclient.publish("/ankursharingan@gmail.com/test2", "50")
time.sleep(3)
mqttclient.publish("/ankursharingan@gmail.com/", "10")
time.sleep(3)'''
cont=1
while cont==1:
    on=0
    for y in range(23):
        #mqttclient.publish("/ankursharingan@gmail.com/", float(moisture_set[y]))
        #time.sleep(3)
        mqttclient.publish("/ankursharingan@gmail.com/test1", float(moisture_set[y]))
        #time.sleep(3)
        mqttclient.publish("/ankursharingan@gmail.com/test2", float(temp_set[y]))
        #time.sleep(3)
        mqttclient.publish("/ankursharingan@gmail.com/test3", float(wat_lvl_set[y]))
        #time.sleep(3)
        if float(moisture_set[y]) < 23.0 :
            mqttclient.publish("/ankursharingan@gmail.com/pump", "On")
            on=1
            #time.sleep(3)
        elif float(moisture_set[y]) > 41.0 :
            mqttclient.publish("/ankursharingan@gmail.com/pump", "Off")
            on=0
            time.sleep(3)
        else :
            if on==0:
                mqttclient.publish("/ankursharingan@gmail.com/pump", "Off")
                #time.sleep(3)
            else:
                mqttclient.publish("/ankursharingan@gmail.com/pump", "On")
                #time.sleep(3)
        print("Loop " + str(y) +" Done")
        time.sleep(3)
    cont=int(input('Enter 1 to continue 0 to exit '))
print("f")

# Loop; exit on error
rc = 0
print(str(rc))
while rc == 0:
    rc = client.loop()
print("rc: " + str(rc))
