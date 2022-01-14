# Tower

The tower is the central element of the playing field. It is used to move the comets around the playing field so every player has a chance to hit them.

<figure markdown>
  ![CAD model of the tower](3D_models/tower/TumV01.png){ height="200"}
  <figcaption>3D CAD model of the tower</figcaption>
</figure>

## Construction

The tower consists of a base and an arm with a comet at each end. The arm can be rotated horizontally and tilted vertically. Both motions are created with a stepper motor. The stepper motors are controlled with the Raspberry Pi using a **Adafruit Motor Shield**.

## Setup

!!! INFO
    The documentation of the software wich is used to control the tower can be found [here](https://4d-game.github.io/Gamecontrol/)

The **Adafruit Motor Shield** can be controlled in python using the [Adafruit CircuitPython MotorKit](https://github.com/adafruit/Adafruit_CircuitPython_MotorKit) library.

Because the **Adafruit Motor Shield** uses **I2C** to communicate with the Raspberry Pi I2C needs to be enabled.

!!! WARNING
    On the Raspberry Pi the I2C speed has to be set to **...**.


## Components

For a list of all used components see the [Components](components.md) section.