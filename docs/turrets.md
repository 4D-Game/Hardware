
# Turrets

The turrets are controlled by the player. They are used to "shoot" the "comets". In the current setup six turrets are used. 


![](assets/turrets1.jpeg)

![](assets/turrets2.jpeg)

![](assets/turrets3.jpeg)

## Construction

### Functionality

The model used for implementing the turrets was found on Thingiverse. We chose this model because the design went very well with our initial game idea and the fundamental movements (Horizontal and vertical rotation of the aiming part) were given. As said, the main technical functionality of this Prototype is to rotate horizontal and vertical in order ot give the player a good aiming experience. One is placed below the base of the turret. The other is placed on the right side of the top element. In order to detect if the player hit the comet a IR-Sensor is used. The model which is used returns a digital signal. The sensitivity can be tuned with a screw on the back of the sensor.Horizontal rotation of the aiming part would be indicated with the help of an RGB NEOPIXEL LED ring.


### Adapted 3D-Models of turrets

![](3D_models/turrets/base.png)
![](3D_models/turrets/base_mount.png)
![](3D_models/turrets/baus_mount.png)
![](3D_models/turrets/laser_arm.png)
![](3D_models/turrets/right_left_bearing_half.png)
![](3D_models/turrets/servo_bracket.png)
![](3D_models/turrets/turret_leg.png)
![](3D_models/turrets/turret_top.png)
![](3D_models/turrets/full_turret.png)


### Adaptations 

This model was not configured for our Servo Motors. Therefore, every 3D-Model that consists part of the motor needed to be changed. For our game, we need something like a gun that can shoot the comets. Therefore the Blaster Model was created.

- Base: New configuration of the middle part. Adapted to fit our servo motor.
- Base_mount: Creating a little motor winding to fit in the base mount.
- Servo_bracket: Adapting the servo bracket to fit our servo motor
- Turret_legs: Added holes for mounting the Turret to the Base plate
- Blaster: New Model which held the Laser sensor, In addition two led's are used to display if the player shot (white) and if he hit (green). Both led's are positioned at the tip of the barrel of the turret.
![](3D_models/Turret/turret_final.png)

![](assets/turret_final_cad1.png)

## Technical characteristics

| Mechanical Device | Action | Description | State |
| --------------- | --------------- | --------------- | --------------- |
| Bottom servo motor | Horizontal Turret motion | Joystick full right / full left | +-30° right/left max |
| Top servo motor | Vertical Turret motion| Joystick full up / full down | +20° top max / -40° bottom max|
| Indicators | Shooting | RED / GREEN LED |  Blinks every shot / Blinks when hit detected |
| Indicators | Shooting | RGB Led Ring | blue at the game start, green if all players ready, show movement of the horizontal servo during play|
| Blaster | Shooting | IR barrier switch| Adjustable detection distance from 3 to 80 cm|

### Circuit (connection ot Raspberry Pi)

![Turrets circuit](circuit/turrets1.png)


## Components

For a list of all used components see the [components](Components.md) section.

## Further information's

All 3D-Models were done with Fusion360.
For more information's about controlling the turrets via controller and software solutions please look [here](4D_Game/Controller/docs/code-references/controls/turrets.md).




