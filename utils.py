#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 9:16
# @Author  : kunkun
# @Email   : yikunwang6@163.com
# @File    : utils.py
# @Software: PyCharm

can_move={0:[1,3],
          1:[0,2,4,],
          2: [1, 5],
          3: [0, 4, 6],
          4: [1, 3, 5, 7],
          5: [2, 4, 8],
          6: [3, 7],
          7: [4, 6, 8],
          8: [5, 7]}

def move(row,col,map):
    if row > col:
        row,col = col,row
    new_map=map[:row]+map[col]+
    return new_map