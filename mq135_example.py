"""MQ135 Module example"""
import time
from MQ135 import MQ135

class mq135lib_example(object):
    """MQ135 lib example"""

    def __init__(self, pin, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.mq135 = MQ135(pin) # analog PIN

    def pprint(self):
        """Continuos print of MQ135 values """

        while True:
            rzero = self.mq135.get_rzero()
            corrected_rzero = self.mq135.get_corrected_rzero(self.temperature, self.humidity)
            resistance = self.mq135.get_resistance()
            ppm = self.mq135.get_ppm()
            corrected_ppm = self.mq135.get_corrected_ppm(self.temperature, self.humidity)

            print("MQ135 RZero: " + str(rzero) +"\t Corrected RZero: "+ str(corrected_rzero)+
                  "\t Resistance: "+ str(resistance) +"\t PPM: "+str(ppm)+
                  "\t Corrected PPM: "+str(corrected_ppm)+"ppm")
            time.sleep(0.3)

if __name__ == "__main__":
    mq = mq135lib_example(0, 21.0, 25.0)
    mq.pprint()
