import pybullet as p
import time

p.connect(p.GUI_SERVER)

while 1:
    p.stepSimulation()
    time.sleep(0.01)