from machine import Pin
import dht
import time
sensor = dht.DHT11(Pin(4))
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(f"温度是{temp}摄氏度,湿度是{hum}")
time.sleep(2)
