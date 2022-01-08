#!/usr/bin/env python3
import os, time
from pygame import mixer

class Music:

    def __init__(self):

        mixer.init()
        # Load the sounds
        self.sound_1 = mixer.Sound('test_1.mp3')
        self.sound_2 = mixer.Sound('test_2.mp3')


    def play(self,event:int):
        if event ==1:
            self.sound_1.play()
            # wait for sound to finish playing
            time.sleep(10)
            self.sound_1.stop()
        if event ==2:
            self.sound_2.play()
            # wait for sound to finish playing
            time.sleep(40)
            self.sound_2.stop()  


if __name__ == "__main__":
    test = Music()
    test.play(1)
    time.sleep(2)
    test.play(2)