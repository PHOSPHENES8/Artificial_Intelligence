#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 9:16
# @Author  : kunkun
# @Email   : yikunwang6@163.com
# @File    : AStar.py
# @Software: PyCharm

from utils import can_move,move,can_move_to

def cal_distance(start,target):#这部分可以放在utils中
    ans = 0
    zero = start.index("0")
    for i in range(0,9):
        if i != zero:
            ans += abs(i - target.index(start[i]))
    return ans

def AStar(start,target):
    if can_move(start,target) == False:
        return -1, None

    path = {start:-1}# 初始化路径记录
    g = {start:1}# 初始化G表
    f = {start: 1+ cal_distance(start,target)}  # 初始化F表
    open  = [start]# 初始化open表
    close = []     # 初始化close表
    current=start

    while len(open) > 0:
        # step1:取open表中最小的值
        current=min(f,key=f.get)
        # step2:更新各项表记录
        open.remove(current)
        close.append(current)
        del f[current]
        # step3:判断是否结束
        if current==target:
            break #成功
        zero = current.index("0")
        can_choose=can_move_to[zero]# 挑选出可以和当前节点进行交换的节点集合
        for item in can_choose:
            new = move(item,zero,current)
            f_value = cal_distance(new,target)#计算新的f值
            if new in close:# 如果新的节点已经再close表中
                continue
            else:
                if new not in open:
                    g[new]=g[current]+1
                    f[new]=f_value
                    path[new]=current#记录父节点
                    open.append(new)
                else:
                    if f[new]>f_value:#此时需要更新信息
                        g[new]=g[current]+1
                        f[new] = f
                        path[new] = current  # 记录父节点

    trace_steps = [target]
    while path[current]!=-1:
        current = path[current]
        trace_steps.append(current)
    trace_steps.reverse()#显示完整路径
    return 0, trace_steps



if __name__ == "__main__":
    start  = "325467018"
    target = "012345678"

    # steps记录序列的逐步变化
    can_reach, steps = AStar(start,target)

    if can_reach == 0:
        for index in range(len(steps)):
            print("Step #" + str(index + 1))
            #打印地图
            print(steps[index][:3])
            print(steps[index][3:6])
            print(steps[index][6:])

    else:
        print("目标布局不可达！")