from .. import utiles
import pybullet as p

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

resetAction = 0
moveAction = 1

currentAction = resetAction