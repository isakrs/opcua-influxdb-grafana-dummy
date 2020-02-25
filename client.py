from opcua import Client
import time


url = "opc.tcp://51.144.139.143:4840"

client = Client(url)

client.connect()
print("client connected")

while True:
	temp = client.get_node("ns=2;i=2")
	temp_value = temp.get_value()

	press = client.get_node("ns=2;i=3")
	press_value = press.get_value()

	timestamp = client.get_node("ns=2;i=4")
	timestamp_value = timestamp.get_value()

	print(temp_value, press_value, timestamp_value)

	time.sleep(1.0)

