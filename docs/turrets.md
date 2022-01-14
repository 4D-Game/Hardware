# Turrets

The turrets are controlled by the player. They are used to "shoot" the "comets". In the current setup six turrets are used.

<figure markdown>
  ![CAD model of a turret](3D_models/turrets/full_turret.png){ width="400" }
  <figcaption>3D CAD model of a turret</figcaption>
</figure>

## Construction

### Turret

The model used for the turrets is based on a model found on [Thingiverse](https://www.thingiverse.com)[^1].

Two servos are used two create horizontal and vertical motion. One is placed below the base of the turret. The other is placed on the right side of the top element.

In order to detect if the player hit the comet a IR-Sensor is used. The model which is used returns a binary signal. The sensitivity can be tuned with a screw on the back of the sensor.

In adition two led's are used to display if the player shot (*white*) and if he hit (*green*). Both led's are positioned at the tip of the barrel of the turret.

### LED Circle

Below the each turret a led circle displays if a player is ready. While the game the circle displays the **...** of the player. The led circle is controlled over a Raspberry Pi using **SPI**

## Components

For a list of all used components see the [Components](components.md) section.

[^1]: **modelname** by **creator** source: [https://www.https://www.thingiverse.com/something](https://www.https://www.thingiverse.com/something)