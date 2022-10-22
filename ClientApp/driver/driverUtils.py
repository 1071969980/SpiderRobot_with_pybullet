from Board import *
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
        return int((angle + pi / 2) / pi * 1000)
    else:
        if id % 3 == 2:
            return int((angle + pi / 2) / pi * 800 + 100)
        else:
            return int((angle + pi * 3 / 4) / (pi * 3 / 2) * 1000)

idMap = [7,8,9,4,5,6,1,2,3,16,17,18,13,14,15,10,11,12]
def convertID(id):
    # Mapping from joint ID in ../spider to ID in control board
    # ignore end point id
    assert id <= 23, "convertID(id): id exceeds the number of joints."
    assert id >= 0, "convertID(id): id < 0"
    assert id % 4 != 3, "convertID(id): id corrsponds to a end joint"
    return idMap[id - id // 4]

def setBusServoAngle(id, angle, use_time=500):
    id = convertID(id)
    pulse = convertAngleToPulse(id, angle)
    setBusServoPulse(id, pulse, use_time)