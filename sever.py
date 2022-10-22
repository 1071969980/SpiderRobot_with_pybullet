import pybullet as p
import time
import sys

local_server = False
try:
    local_server = sys.argv[1] == "-local"
except:
    pass

if local_server:
    p.connect(p.GUI_SERVER)
    while p.isConnected():
        p.stepSimulation()
        time.sleep(1. / 240.)

else:
    p.connect(p.GRAPHICS_SERVER)

    print("started graphics server")
    while p.isConnected():
        time.sleep(1. / 240.)