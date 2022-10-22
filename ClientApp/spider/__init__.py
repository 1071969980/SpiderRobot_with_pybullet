import numpy as np

FrontLeftEndId = 3
MidLeftEndId = 7
BackLeftEndId = 11
FrontRightEndId = 15
MidRightEndId = 19
BackRightEndId = 23

frontLeftEndPos = np.zeros(3)
midLeftEndPos = np.zeros(3)
backLeftEndPos = np.zeros(3)
frontRightEndPos = np.zeros(3)
midRightEndPos = np.zeros(3)
backRightEndPos = np.zeros(3)

resetFrontLeftEndPos = np.zeros(3)
resetMidLeftEndPos = np.zeros(3)
resetBackLeftEndPos = np.zeros(3)
resetFrontRightEndPos = np.zeros(3)
resetMidRightEndPos = np.zeros(3)
resetBackRightEndPos = np.zeros(3)

# 动作组，是对应LinkEnd与动作曲线的字典
resetAction = {}
moveAction = {}

currentAction = resetAction

def recordResetPos():
    """
    用当前姿态设置成静止姿态
    :return:
    """
