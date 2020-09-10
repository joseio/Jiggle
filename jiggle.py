#!/usr/bin/python

# Above allows it to run from terminal w/o needing to type full path 

from pynput.mouse import Button, Controller
import time

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
  mouse.position))

# Set pointer position
mouse.position = (0, 10)
print('Now we have moved it to {0}'.format(
   mouse.position))

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
 

