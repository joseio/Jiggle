#!/usr/bin/python
# Above allows it to run from terminal by simply typing `jiggle.py`
# You may need to change the path on line 1 to account for where Python is installed on your system
# Type `which python` in the terminal to find out the correct path you need to use

from pynput.mouse import Button, Controller
import time

mouse = Controller()

# Read pointer position
print('Now jiggling...')

# Set pointer position
mouse.position = (0, 10)

# Move pointer relative to current position every 10 min
def jiggle():
  mouse.move(0, -1)
  mouse.move(0, +1)

starttime = time.time()

# Jiggle mouse every 10 minutes
minutes = 10.0
delay = 60 * minutes
while True:
  jiggle()
  time.sleep(delay - ((time.time() - starttime) % delay))
