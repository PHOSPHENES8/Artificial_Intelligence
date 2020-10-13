#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 9:16
# @Author  : kunkun
# @Email   : yikunwang6@163.com
# @File    : utils.py
# @Software: PyCharm

can_move_to={0: [1,3],
             1: [0,2,4,],
             2: [1, 5],
             3: [0, 4, 6],
             4: [1, 3, 5, 7],
             5: [2, 4, 8],
             6: [3, 7],
             7: [4, 6, 8],
             8: [5, 7]}

def cal_reverse(sequence):#计算sequence序列的逆序对
    ans=0
    for i in range(1,9):#从第二个数字开始计算
        for j in range(i):#和当前数字前面的数字逐个比较
            if sequence[j]>sequence[i] and sequence[i] != '0':#这里不需要第二个条件也可以
                ans = ans + 1
    return ans

def move(row,col,map):
    if row > col:
        row,col = col,row
    new_map=map[:row]+map[col]+map[row+1:col]+map[row]+map[col+1:]
    return new_map

def can_move(start,target):#通过逆序对判断两个状态是否可互通
    start_reverse  = cal_reverse(start)
    target_reverse = cal_reverse(target)
    if(start_reverse % 2) != (target_reverse % 2): #如果两个状态的逆序对的奇偶性不同，则返回False
        return False
    return True