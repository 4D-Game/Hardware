# **Motor Control**

## **Control with adafruit motor shield on raspberry pi**

![Adafruit Motorshield for dc & stepper motors](pictures/Adafruit_motorshield.jpeg)

**Instruction to set up Motorshield**

https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi

**Datasheet**

![adafruit_datasheet](datasheet/2348_ENG_TDS.pdf)


**Assembled**

![Adafruit assembled](pictures/adafruit_assembled.jpeg)

**Git Repository**

https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git


**Testcode for a DC motor**

```c

from adafruit_motorkit import MotorKit
kit = MotorKit()
kit.motor1.throttle = 0.1

```
