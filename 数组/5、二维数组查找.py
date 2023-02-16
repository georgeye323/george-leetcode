"""
在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]
给定 target = 7，返回 true。

给定 target = 3，返回 false。
"""

def solution(target: int, array: list)-> bool:
    # 判断特殊情况
    if len(array) == 0:
        return  False
    if len(array[0]) == 0:
        return False
    n = len(array)
    i = n - 1
    m = len(array[0])
    j = 0
    # 从最左下角的元素开始往左或往上
    while i >= 0 and j < m:
        # 元素较大, 往上走
        if array[i][j] > target:
            i -= 1
        elif array[i][j] < target:
            j += 1
        else:
            return True
    return False
