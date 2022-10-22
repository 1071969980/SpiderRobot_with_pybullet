import pybullet as p
import time

p.connect(p.DIRECT)

while 1:
    p.stepSimulation()
    time.sleep(0.01)