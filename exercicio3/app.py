import paho.mqtt.client as mqtt
import random
import time

THE_BROKER = "test.mosquitto.org"
THE_TOPIC = "app/autizapy/grupo"
CLIENT_ID = ""

# The callback for when the client receives a CONNACK 
# response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)


# The callback for when a message is received from the server.
def on_message(client, userdata, msg):
    print("sisub: msg received with topic: {} and payload: {}".format(msg.topic, str(msg.payload)))


client = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(None, password=None)
client.connect(THE_BROKER, port=1883, keepalive=60)

client.loop_start()


while True:
    print(f"Topico: {THE_TOPIC}")
    print("Digite sua mensagen abaixo")
    client.on_message = on_message

    mensagem_para_enviar = input()
    
    if mensagem_para_enviar.lower() == 'sair':
        break
        
    client.publish(THE_TOPIC, mensagem_para_enviar)
    time.sleep(0.2) 
