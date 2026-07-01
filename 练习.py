import time
import dht
from machin import Pin
import network
import urequests

#连wifi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("wifi账号是","wifi密码是")
while not wifi.isconnected():
    time.sleep(1)
print("wifi已连接",wifi.ifconfig())
#创建传感器
sensor = dht.DHT11(Pim(4))
#循环读取
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()

    data = {"temperature":temp,"humidity":hum}
    response = urequests.post(SERVER_URL,json=data)
    print(response.text)
    response.close()
    time.sleep(2)