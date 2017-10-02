import time
from dht import DHT11
from machine import Pin
from MQ135 import MQ135


# setup
mq135 = MQ135(0) # analog PIN 0
dht11 = DHT11(Pin(4)) # D2

# loop
while True:

    dht11.measure()
    temperature = dht11.temperature()
    humidity = dht11.humidity()

    rzero = mq135.get_rzero()
    corrected_rzero = mq135.get_corrected_rzero(temperature, humidity)
    resistance = mq135.get_resistance()
    ppm = mq135.get_ppm()
    corrected_ppm = mq135.get_corrected_ppm(temperature, humidity)

    print("DHT11 Temperature: " + str(temperature) +"\t Humidity: "+ str(humidity))
    print("MQ135 RZero: " + str(rzero) +"\t Corrected RZero: "+ str(corrected_rzero)+
          "\t Resistance: "+ str(resistance) +"\t PPM: "+str(ppm)+
          "\t Corrected PPM: "+str(corrected_ppm)+"ppm")
    time.sleep(1)
