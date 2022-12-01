"""
leetcode 209
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""

def solution(target: int, nums: list)->list:
    left = 0
    n = len(nums)
    res = float('inf')
    num_sum = 0
    for r in range(n):
        num_sum += nums[r]
        while num_sum >= target:
            res = min(r-left+1, res)
            num_sum -= nums[left]
            left += 1
    return 0 if res == float("inf") else res

print(solution(7,  [2,3,1,2,4,3]))


