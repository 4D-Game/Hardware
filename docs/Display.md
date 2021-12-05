**Display**

Test with two 2.2 TFT SPI 240x320 Displays and RaspberryPi 3B.


**Setup**

raspi-config -> SPI enable

sudo pip3 install Adafruit-Blinka

sudo pip3 install adafruit-circuitpython-rgb-display

sudo apt-get install python3-pil

sudo reboot

**Examples**

https://learn.adafruit.com/2-2-tft-display/python-usage

![Display test](pictures/display_test.jpeg)

**Pinout**

Display-> Pi

CLK -> SLCK

MOSI -> MOSI

CS -> CE0

D/C -> GPIO 25

RESET -> GPIO 24

Vin -> 3.3V

GND -> GND

LED -> 3.3V



