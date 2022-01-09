# Sound

sudo apt-get install alsa-utils

sudo aplay -l check device ID 

sudo nano /usr/share/alsa/alsa.conf
change :

defaults.ctl.card "ID"

defaults.pcm.card "ID"

sudo apt-get install python3-pygame
sudo apt-get install python3-sdl2

https://www.python-lernen.de/pygame-spiele-sound-hintergrundmusik.htm
https://mixkit.co/free-sound-effects/game/?page=3