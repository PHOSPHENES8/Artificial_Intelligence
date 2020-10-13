from function import *


def calc_hn(curLayout, destLayout):
    """ 计算hn,即当前状态距离目标状态的距离

    :param curLayout: 当前状态
    :param destLayout: 目标状态
    :return: hn
    """
    cnt = 0
    a = curLayout.index("0")
    for i in range(0, 9):
        if i != a:
            cnt += abs(i - destLayout.index(curLayout[i]))
    return cnt


def Astar(srcLayout, destLayout):
    # 先进行判断srcLayout和destLayout逆序值是否同是奇数或偶数
    if not check(srcLayout, destLayout):
        return -1, None

    # 初始化
    dict_road = {srcLayout: -1}  # 路径
    dict_gn = {srcLayout: 1}  # gn
    dict_fn = {srcLayout: 1+calc_hn(srcLayout, destLayout)}  # fn
    OPEN = [srcLayout]  # OPEN表
    CLOSE = []
    curLayout = srcLayout

    while len(OPEN) > 0:
        curLayout = min(dict_fn, key=dict_fn.get)  # 取open队列中最小的fn
        del dict_fn[curLayout]
        OPEN.remove(curLayout)  # 找到最小fn，并移除
        CLOSE.append(curLayout)  # 当前节点进close表
        if curLayout == destLayout:  # 判断当前状态是否为目标状态
            break
        # 寻找0 的位置。
        ind_slide = curLayout.index("0")
        lst_shifts = dict_shifts[ind_slide]  # 当前可进行交换的位置集合
        for nShift in lst_shifts:
            newLayout = swap_chr(curLayout, nShift, ind_slide)  # 得到扩展的新节点
            fn = calc_hn(newLayout, destLayout) + 1 + dict_gn[curLayout]  # 计算新的fn
            if newLayout in CLOSE:  # 新节点在CLOSE中
                continue
            else:  # 新节点不再CLOSE中
                if newLayout not in OPEN:  # 新节点不在OPEN中
                    dict_gn[newLayout] = dict_gn[curLayout] + 1  # 存入深度
                    dict_fn[newLayout] = fn  # 存入fn
                    dict_road[newLayout] = curLayout  # 定义前驱结点
                    OPEN.append(newLayout)  # 存入集合
                else:  # 新节点不在CLOSE但在OPEN中
                    if dict_fn[newLayout] > fn:  # 并且fn小于之前的fn
                        dict_gn[newLayout] = dict_gn[curLayout] + 1  # 存入深度
                        dict_fn[newLayout] = fn  # 存入fn
                        dict_road[newLayout] = curLayout  # 定义前驱结点

    last_steps = [destLayout]
    while dict_road[curLayout] != -1:  # 存入路径
        curLayout = dict_road[curLayout]
        last_steps.append(curLayout)
    last_steps.reverse()
    return 0, last_steps




if __name__ == "__main__":
    # 测试数据
    src = "015326748"
    dest = "123456780"

    retCode, lst_steps = Astar(src, dest)
    if retCode != 0:
        print("目标布局不可达")
    else:
        for nIndex in range(len(lst_steps)):
            print("step #" + str(nIndex + 1))
            print(lst_steps[nIndex][:3])
            print(lst_steps[nIndex][3:6])
            print(lst_steps[nIndex][6:])
