from pygame import mixer
import os
import time

mixer.pre_init(44100, -16, 2, 4096)
mixer.init()
mixer.music.load('se/bgm.wav')
mixer.music.play(loops=-1)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    mixer.music.stop()
#se1 = mixer.Sound('se/bgm.wav')
#se1.play()
#time.sleep(5)
