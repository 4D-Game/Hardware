# Displays

With the displays the points of every team as well as the winner is displayed. In adition this module provides some soundeffects using a speakter

## Construction

### Displays



#### Connection to Raspberry Pi
```
Display   -> Pi
CLK       -> SLCK
MOSI      -> MOSI
CS        -> CE0
D/C       -> GPIO 25
RESET     -> GPIO 24
Vin       -> 3.3V
GND       -> GND
LED       -> 3.3V
```

!!! NOTE
    Both displays are connected to the same pins so they show the same image


### Speaker
## Setup

!!! INFO
    The documentation of the software wich is used to control displays and speaker in the game can be found [here](https://4d-game.github.io/Gamecontrol/)
### Displays

In order to use the diplays in a python program on a raspberry pi **SPI** needs to be enabled.

Next the following commands need to be executed to install the packages needed to communicate with the Displays.

```bash
sudo pip3 install Adafruit-Blinka
sudo pip3 install adafruit-circuitpython-rgb-display
sudo apt-get install python3-pil
```

!!! NOTE
    After installing those packages a reboot is necessary


!!!INFO
    Examples on how to use the displays can be found [here](https://learn.adafruit.com/2-2-tft-display/python-usage)

![Display test](pictures/display_test.jpeg)

