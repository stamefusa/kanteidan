from pygame import mixer
import os
import time

mixer.pre_init(44100, -16, 2, 4096)
mixer.init()
se1 = mixer.Sound('se/1.wav')
se1.play()
time.sleep(1)
