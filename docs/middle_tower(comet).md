
## Tower

The tower is the central element of the playing field. It is used to move the comets around the playing field so every player has a chance to hit them.

![View from the top](assets/tower2.jpeg)

![View from the side](assets/tower1.jpeg)

## Construction

### Functionality

The tower consists of a base and an arm with a comet at each end. The arm can be rotated horizontally and tilted vertically. Both motions are created with a stepper motor. The stepper motors are controlled with the Raspberry Pi using a Adafruit Motor Shield. In order to avoid too far tilting to the right and to the left, 2 end stoppers and physical limitation are built in.

(mechanical aufbau)
## Technical characteristics

The arm can be tilted vertically +-16° right/left max.
The arm rotates in a circle during the game.

### Adapted 3D-Model of middle Tower

![Middle Tower](3D_models/Tower/middle_Tower_png.png)

### Circuit (connection to Raspberry Pi)

![Middle Tower circuit](circuit/middle_tower1.png)

For the connection between motors, motorshield to Raspberry Pi see [here](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/stacking-hats)


## Components

For a list of all used components see the [Components](Components.md) section.

## Further informations

All 3D-Models were done with Fusion360.
For informations about controlling the turrets via controller and software solutions please look here

