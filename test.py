# Sound1a.py

import time
from soundplayer import SoundPlayer

# Use device with ID 1  (mostly USB audio adapter)
p = SoundPlayer("hello.mp3", 1)        
print "playing"
p.play() # non-blocking, volume = 0.5
print "done"