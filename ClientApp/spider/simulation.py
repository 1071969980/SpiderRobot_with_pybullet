# 这个文件包含对目标点和IK计算的线程
import Action


# todo 包装成多线程函数，访问目标位置时上锁
def calculateTargetPos():
    """
    使用动作描述类，按时间和计算目标点
    :return:
    """


# todo 包装成多线程函数，访问目标位置时上锁
def step():
    """
    使用目标位置来循环调用ik模拟
    :return:
    """


def recordResetPos():
    """
    用当前姿态设置成静止姿态
    :return:
    """
