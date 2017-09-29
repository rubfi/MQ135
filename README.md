# MQ135 - Micropython
Micropython library for dealing with MQ135 gas sensor

Based on the Arduino library developed by G.Krocker (Mad Frog Labs) and the corrections from balk77 and ViliusKraujutis
  
More info:
  * https://hackaday.io/project/3475-sniffing-trinket/log/12363-mq135-arduino-library
  * https://github.com/ViliusKraujutis/MQ135
  * https://github.com/balk77/MQ135

## Usage
You can use ampy (https://github.com/adafruit/ampy) for uploading the files to the device

```
ampy put mq135_example.py
ampy put mq135.py
ampy run -n mq135_example.py
```
and then connect to the device with the serial comunication program (e.g: *minicom*) in order to see the output

*Note: MQ135 sensor is connected to A0 in the example*

if you want to load the code at the device boot
```
ampy put mq135.py main.py
```
## Notes
*Tested with Micropython for the ESP8266.*
