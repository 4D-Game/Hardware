```
import processing.serial.*;

import cc.arduino.*;

Arduino arduino;

void setup() 
{
  size(460, 300);
  
  // Prints out the available serial ports.
  println(Arduino.list());
  
  // Modify this line, by changing the "0" to the index of the serial
  // port corresponding to your Arduino board (as it appears in the list
  // printed by the line above).
  arduino = new Arduino(this, Arduino.list()[0], 57600);
  
  // Alternatively, use the name of the serial port corresponding to your
  // Arduino (in double-quotes), as in the following line.
  //arduino = new Arduino(this, "/dev/tty.usbmodem621", 57600);
  
  // Configure digital pins 4 and 7 to control servo motors.
  arduino.pinMode(10, Arduino.SERVO);
  arduino.pinMode(9, Arduino.SERVO);
}

void draw() 
{
  background(constrain(mouseX / 2, 100, 255));
  
  // Write an value to the servos, telling them to go to the corresponding
  // angle (for standard servos) or move at a particular speed (continuous
  // rotation servos).
  arduino.servoWrite(9, constrain(180 - mouseX / 2, 0, 80));
  arduino.servoWrite(10 , constrain(180 - mouseY / 2, 0, 80));
}


```