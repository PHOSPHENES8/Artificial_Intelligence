#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 9:16
# @Author  : kunkun
# @Email   : yikunwang6@163.com
# @File    : BFS.py
# @Software: PyCharm

from utils import *

def BFS(start,target):
    if can_move(start,target) == False:
        return -1, None

    current=start
    open=[start]
    path={start:-1}
    while len(open)>0:
        # step1:pop队列中第一个元素
        current=open.pop(0)
        if current == target:
            break
        zero=current.index("0")
        can_choose = can_move_to[zero]  # 挑选出可以和当前节点进行交换的节点集合
        for item in can_choose:
            new = move(item,zero,current)
            if path.get(new) is None:# not visited
                path[new]=current#记录父节点
                open.append(new)

    trace_steps = [target]
    while path[current] != -1:
        current = path[current]
        trace_steps.append(current)
    trace_steps.reverse()  # 显示完整路径
    return 0, trace_steps


if __name__ == "__main__":
    start  = "325467018"
    target = "012345678"

    # steps记录序列的逐步变化
    can_reach, steps = BFS(start,target)

    if can_reach == 0:
        for index in range(len(steps)):
            print("Step #" + str(index + 1))
            #打印地图
            print(steps[index][:3])
            print(steps[index][3:6])
            print(steps[index][6:])

    else:
        print("目标布局不可达！")