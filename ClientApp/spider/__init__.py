# 这个库定义和进行虚拟蜘蛛的动作模拟

import numpy as np
import simulation


FrontLeftEndId = 3
MidLeftEndId = 7
BackLeftEndId = 11
FrontRightEndId = 15
MidRightEndId = 19
BackRightEndId = 23

# 关节目标点
frontLeftEndPos = np.zeros(3)
midLeftEndPos = np.zeros(3)
backLeftEndPos = np.zeros(3)
frontRightEndPos = np.zeros(3)
midRightEndPos = np.zeros(3)
backRightEndPos = np.zeros(3)

# 关节静止位置
resetFrontLeftEndPos = np.zeros(3)
resetMidLeftEndPos = np.zeros(3)
resetBackLeftEndPos = np.zeros(3)
resetFrontRightEndPos = np.zeros(3)
resetMidRightEndPos = np.zeros(3)
resetBackRightEndPos = np.zeros(3)

# 当前动作
currentAction = None


def changeAction():
    """
    改变当前动作，通过读取配置文件并且，对currentAction赋值为新的Action实例
    :return:
    """