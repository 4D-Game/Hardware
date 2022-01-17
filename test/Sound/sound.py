from pygame import mixer
import time

class Sound:
    """
        Class for managing sounds during the game
    """

    def __init__(self):
        """
            Configures the mixer to play and load needed sounds
        """
        mixer.init()
        self.shoot_sound = mixer.Sound('/home/pi/sounds_effect/laser-shoot.wav')
        self.score_sound = mixer.Sound('intro.wav')
       
    def play_sound(self, event: int):
        """
            Plays sound depending on event (score, shoot)
        """
        if event == 1:
            self.shoot_sound.set_volume(10)
            self.shoot_sound.play()

        elif event == 2:
            self.score_sound.set_volume(10)
            self.score_sound.play() 


    def stop_sound(self, event: int):
        """
            Stops sound depending on the event
        """
        if event == 1:
            self.shoot_sound.stop()
        elif event == 2:
            self.score_sound.stop() 

if __name__ == "__main__":
    test = Sound()
    
    test.play_sound(1)
    time.sleep(3) #just for the test
    test.stop_sound(1)
    time.sleep(2)
    test.play_sound(2)
    time.sleep(10) #just for the test
    test.stop_sound(2)