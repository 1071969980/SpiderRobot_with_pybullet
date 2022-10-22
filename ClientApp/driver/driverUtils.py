from Board import *
import math
from math import pi
import pybullet as p

def convertAngleToPulse(id, angle):
    # 将弧度转化为内部角度值(0-1000)
    # :param id 舵机编号
    # :param angle 角度（弧度输入）
    
    # 第一关节 -90度~90度 0~1000
    # 第二关节 -90度~90度 100~900
    # 第三关节 -135度~135度 0~1000
    if id % 3 == 1:
        return (angle + pi / 2) / pi * 1000
    else:
        if id % 3 == 2:
            return (angle + pi / 2) / pi * 800 + 100
        else:
            return (angle + pi * 3 / 4) / (pi * 3 / 2) * 1000

# Mapping from ID in ../spider to true ID
def convertID(id):
    return id

def setBusServoAngle(id, angle, use_time):
    pulse = convertAngleToPulse(id, angle)
    id = convertID(id)
    setBusServoPulse(id, pulse, use_time)