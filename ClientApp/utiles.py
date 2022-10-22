import pybullet as p

SpiderId = -1
jointNum = -1
jointInfoList = []
jointStateList = []
linkStateList = []


def connect():
    """
    链接物理引擎并且载入蜘蛛文件
    :return:
    """
    p.connect(p.SHARED_MEMORY)
    global SpiderId, jointNum
    SpiderId = p.loadURDF(r"/home/pi/SpiderRobot_with_pybullet/URDF/Spider.SLDASM/urdf/Spider.SLDASM.urdf", [0, 0, 0], useFixedBase=1)
    jointNum = p.getNumJoints(0)


def getAllJointInfo():
    jointInfoList.clear()
    for i in range(jointNum):
        jointInfoList.append(p.getJointInfo(SpiderId, i))


def getAllJointState():
    global jointStateList
    jointStateList = p.getJointStates(SpiderId, range(jointNum))


def iterMovableJoint():
    for i in range(jointNum):
        if jointInfoList[i][2] != 4:
            yield i


def getAllLinkState():
    global linkStateList
    linkStateList = p.getLinkStates(SpiderId, range(jointNum))


def moveWithIK(endlinkId, pos, useSimulation=True, gain=0.8):
    """
    使用ik移动关节
    :param endlinkId: 要控制的关节末端
    :param pos: ik的目标点
    :param useSimulation: 是否使用电机模拟
    :param gain: 位置增益
    :return:
    """
    ik_pos = p.calculateInverseKinematics(SpiderId, endlinkId, pos)
    movableJointIdIter = iterMovableJoint()
    if useSimulation:
        for i in range(len(ik_pos)):
            p.setJointMotorControl2(SpiderId,
                                    next(movableJointIdIter),
                                    p.POSITION_CONTROL,
                                    ik_pos[i],
                                    positionGain=gain)
    else:
        for i in range(len(ik_pos)):
            p.resetJointState(SpiderId,
                              next(movableJointIdIter),
                              ik_pos[i])


def close():
    """
    关闭与物理引擎的链接
    """
    p.removeBody(SpiderId)
    p.disconnect()

