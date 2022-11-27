"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
"""

def solution(lst: list, target: int)->int:
    n = len(lst)
    left = 0
    right = n - 1
    while left <= right:
        # 左闭合右闭合
        mid = (left + right) // 2
        if lst[mid] < target:
            # 在右侧
            left = mid + 1
        elif lst[mid] > target:
            # 在左侧
            right = mid - 1
        else:
            return mid

    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(solution(nums, target))
