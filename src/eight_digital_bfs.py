from function import *


def bfs(srcLayout, destLayout):
    """ 广度优先搜索解八数码

    :param srcLayout: 初始布局
    :param destLayout: 目标布局
    :return:
    """
    # 先进行判断srcLayout和destLayout逆序值是否同是奇数或偶数
    # 这是判断起始状态是否能够到达目标状态，同奇同偶时才是可达

    if not check(srcLayout, destLayout):
        return -1, None

    curLayout = srcLayout
    queue = [srcLayout]
    dict_layouts = {srcLayout: -1}  # 定义一个map，记录路径
    while len(queue) > 0:
        curLayout = queue.pop(0)  # 队头出队
        if curLayout == destLayout:  # 判断当前状态是否为目标状态
            break
        ind_slide = curLayout.index("0")  # 寻找0 的位置。
        lst_shifts = dict_shifts[ind_slide]  # 当前可进行交换的位置集合
        for nShift in lst_shifts:
            newLayout = swap_chr(curLayout, nShift, ind_slide)
            if dict_layouts.get(newLayout) is None:  # 判断交换后的状态是否已经查询过
                dict_layouts[newLayout] = curLayout  # 当前状态指向上一个状态
                queue.append(newLayout)  # 存入集合

    lst_steps = [destLayout]
    while dict_layouts[curLayout] != -1:  # 存入路径
        curLayout = dict_layouts[curLayout]
        lst_steps.append(curLayout)
    lst_steps.reverse()
    return 0, lst_steps


if __name__ == "__main__":
    # 测试数据输入格式
    src = "012345678"
    dest = "123456780"

    retCode, last_steps = bfs(src, dest)
    if retCode != 0:
        print("目标布局不可达")
    else:
        for nIndex in range(len(last_steps)):
            print("step #" + str(nIndex + 1))
            print(last_steps[nIndex][:3])
            print(last_steps[nIndex][3:6])
            print(last_steps[nIndex][6:])
