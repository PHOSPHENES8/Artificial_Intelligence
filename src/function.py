dict_shifts = {0: [1, 3],  # 每个位置可交换的位置集合
               1: [0, 2, 4],
               2: [1, 5],
               3: [0, 4, 6],
               4: [1, 3, 5, 7],
               5: [2, 4, 8],
               6: [3, 7],
               7: [4, 6, 8],
               8: [5, 7]}


def swap_chr(a, i, j):
    """ 交换八数码a中ij位置

    :param a: 当前状态
    :param i: 待交换元素1的位置
    :param j: 待交换元素2的位置
    :return: 交换ij之后的状态
    """
    if i > j:  # 保证i<j
        i, j = j, i
    b = a[:i] + a[j] + a[i + 1:j] + a[i] + a[j + 1:]
    return b


def calc_reverse(s):
    """ 计算一个状态下逆序对数量

    :param s: 八数码的状态
    :return: 逆序对数量
    """
    cnt = 0
    for i in range(1, 9):
        for j in range(i):
            if s[j] > s[i] and s[i] != '0':
                cnt += 1
    return cnt


def check(srcLayout, destLayout):
    """ 利用状态的逆序对奇偶性检查能否两个状态能否互通

    :param srcLayout: 初始状态
    :param destLayout: 终末状态
    :return: True or False
    """
    src_reverse = calc_reverse(srcLayout)
    dest_reverse = calc_reverse(destLayout)
    if (src_reverse % 2) != (dest_reverse % 2):  # 一个奇数一个偶数，不可达
        return False
    return True
