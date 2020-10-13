import tkinter as tk
from eight_digital_astar import *
from eight_digital_bfs import *
from function import *
import time


def output(lst):
    j = -2
    for i in range(9):
        if i % 3 == 0:
            j += 2
        if lst[i] == 0:
            label1 = tk.Label(root, text='',
                              bg='#F8F8FF', font=('Arial', 35),
                              width=6, height=3)
        else:
            label1 = tk.Label(root, text=lst[i],
                              bg='#F8F8FF', font=('Arial', 35),
                              width=6, height=3)
        label1.grid(row=j, column=(i % 3), rowspan=2, padx=4, pady=4, sticky='n,e,w,s')
    root.update()


def cc():
    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)


def solve():
    srcLayout = str(ent1.get())
    destLayout = str(ent2.get())
    retCode, lst_steps = Astar(srcLayout, destLayout)
    if retCode != 0:
        txt4.configure(text='否', font=('Arial', 20), fg='red')
    else:
        txt4.configure(text='是', font=('Arial', 20), fg='red')
        lst = []
        cnt = 0
        for item in lst_steps:
            lst.clear()
            print(cnt)
            txt3.configure(text=str(cnt), font=('Arial', 20))
            cnt += 1
            for i in item:
                lst.append(int(i))
            output(lst)
            time.sleep(0.5)

def solve_bfs():
    srcLayout = str(ent1.get())
    destLayout = str(ent2.get())
    retCode, lst_steps = bfs(srcLayout, destLayout)
    if retCode != 0:
        txt4.configure(text='否', font=('Arial', 20), fg='red')
    else:
        txt4.configure(text='是', font=('Arial', 20), fg='red')
        lst = []
        cnt = 0
        for item in lst_steps:
            lst.clear()
            print(cnt)
            txt3.configure(text=str(cnt), font=('Arial', 20))
            cnt += 1
            for i in item:
                lst.append(int(i))
            output(lst)
            time.sleep(0.5)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("八数码")

    root.geometry("750x420")
    frame1 = tk.Frame(root, width=400, height=420, bg='#87CEEB').grid(rowspan=6, columnspan=3)
    # frame2 = tk.Frame(root, width=400, height=420, bg='#E0FFFF', ).grid(row=0, column=3)
    lab1 = tk.Label(root, text='初始状态', font=('Arial', 20))
    lab2 = tk.Label(root, text='终止状态', font=('Arial', 20))
    lab3 = tk.Label(root, text='当前步数', font=('Arial', 20))
    lab4 = tk.Label(root, text='求解状态', font=('Arial', 20))
    bton1 = tk.Button(root, text='Astar', font=('Arial', 20), command=solve)
    bton1_1 = tk.Button(root, text='BFS', font=('Arial', 20), command=solve_bfs)
    bton2 = tk.Button(root, text='清空', font=('Arial', 20), command=cc)
    
    lab5 = tk.Label(root, text='——by 金苡萱', font=('Arial', 20))
    lab1.place(x=420, y=20, width=80, height=60)
    lab2.place(x=420, y=100, width=80, height=60)
    lab3.place(x=420, y=180, width=80, height=60)
    lab4.place(x=420, y=260, width=80, height=60)
    bton1.place(x=420, y=330, width=90, height=40)
    bton1_1.place(x=530, y=330, width=90, height=40)
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
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    output(lst)

    root.mainloop()
