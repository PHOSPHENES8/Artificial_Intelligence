#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 13:08
# @Author  : kunkun
# @Email   : yikunwang6@163.com
# @File    : show.py
# @Software: PyCharm
import tkinter as tk
import time


def printMap(map):
    j = -2
    for i in range(9):
        if i % 3 == 0:
            j += 2
        if map[i] == 0:
            label1 = tk.Label(root,text='',bg='#F8F8FF', font=('Comic Sans MS', 32),width=1,height=1)
        else:
            label1 = tk.Label(root,text=map[i],bg='#F8F8FF', font=('Comic Sans MS', 32),width=2, height=2)
        label1.grid(row=j,column=(i%3),rowspan=2, padx=4, pady=4, sticky='n,e,w,s')
    root.update()

from utils import *
from BFS import *
from AStar import *


def solve_astar():
    start  = str(ent1.get())
    target = str(ent2.get())
    can_reach, steps = AStar(start,target)
    if can_reach != 0:
        txt4.configure(text='未找到求解方法，请尝试其他状态', font=('Comic Sans MS', 14), fg='pink')
    else:
        txt4.configure(text='找到求解方法，正在运行', font=('Comic Sans MS', 14), fg='green')
        map=[]
        cnt=0
        for item in steps:
            map.clear()
            print(cnt)
            txt3.configure(text=str(cnt), font=('Comic Sans MS', 20))
            cnt = cnt + 1
            for i in item:
                map.append(int(i))
            printMap(map)
            time.sleep(0.5)

def solve_bfs():
    start = str(ent1.get())
    target = str(ent2.get())
    # can_reach, steps = BFS(start, target)
    pass



def clear():
    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)


if __name__ == '__main__':
    root=tk.Tk()
    root.title("八数码效果展示   2018302405-王翊堃 ")
    root.geometry("750x420")
    frame1 = tk.Frame(root, width=400, height=420, bg='#f8c382').grid(rowspan=6, columnspan=3)
    # frame2 = tk.Frame(root, width=400, height=420, bg='#E0FFFF', ).grid(row=0, column=3)

    lab1 = tk.Label(root, text='Start', font=('Comic Sans MS', 16))
    lab2 = tk.Label(root, text='Target', font=('Comic Sans MS', 16))
    lab3 = tk.Label(root, text='Step', font=('Comic Sans MS', 16))
    lab4 = tk.Label(root, text='Stutus', font=('Comic Sans MS', 16))
    bton1_1 = tk.Button(root, text='Astar', font=('Comic Sans MS', 16), command=solve_astar)
    bton1_2 = tk.Button(root, text='BFS', font=('Comic Sans MS', 16), command=solve_bfs)
    bton2 = tk.Button(root, text='Clear', font=('Comic Sans MS', 16), command=clear)

    lab5 = tk.Label(root, text='2018302405-王翊堃', font=('Comic Sans MS', 12))

    lab1.place(x=420, y=20, width=80, height=60)
    lab2.place(x=420, y=100, width=80, height=60)
    lab3.place(x=420, y=180, width=80, height=60)
    lab4.place(x=420, y=260, width=80, height=60)
    bton1_1.place(x=420, y=330, width=90, height=40)
    bton1_2.place(x=530, y=330, width=90, height=40)
    bton2.place(x=640, y=330, width=90, height=40)
    lab5.place(x=550, y=380, width=200, height=40)

    ent1 = tk.Entry(root)
    ent1.place(x=520, y=20, width=210, height=60)
    ent2 = tk.Entry(root)
    ent2.place(x=520, y=100, width=210, height=60)
    txt3 = tk.Label(root)
    txt3.place(x=520, y=180, width=210, height=60)
    txt4 = tk.Label(root)
    txt4.place(x=520, y=260, width=210, height=60)

    map=[1,2,3,4,5,6,7,8,0]
    printMap(map)

    root.mainloop()