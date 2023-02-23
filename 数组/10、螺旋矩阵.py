"""
leetcode 59
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
"""


def solution(n: int)->list:
    # 1、生成矩阵
    result =[[0] * n for _ in range(n)]
    # 起始位置
    start_x, start_y = 0, 0
    # 控制循环
    loop = n // 2
    count = 1
    for offset in range(1, loop+1):
        # 从左到右
        for i in range(start_y, n-offset):
            result[start_x][i] = count
            count += 1
        # 从上到下
        for i in range(start_x, n-offset):
            result[i][n-offset] = count
            count += 1
        # 从右到左
        for i in range(n-offset, start_y, -1):
            result[n-offset][i] = count
            count += 1
        # 从下往上
        for i in range(n-offset, start_x, -1):
            result[i][start_y] = count
            count += 1
        start_x += 1
        start_y += 1
    # 如果n为奇数，存在中心点
    if n % 2 != 0:
        result[n//2][n//2] = count
    return result


print(solution(n=2))