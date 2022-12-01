"""
牛客BN19 寻找峰值
给定一个长度为n的数组nums，请你找到峰值并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个所在位置即可。
1.峰值元素是指其值严格大于左右相邻值的元素。严格大于即不能有等于
2.假设 nums[-1] = nums[n] = -\infty−∞
3.对于所有有效的 i 都有 nums[i] != nums[i + 1]
4.你可以使用O(logN)的时间复杂度实现此问题吗？

数据范围：
  
5

-2^{31}<= nums[i] <= 2^{31} - 1−2
31
 <=nums[i]<=2
31
 −1

如输入[2,4,1,2,7,8,4]时，会形成两个山峰，一个是索引为1，峰值为4的山峰，另一个是索引为5，峰值为8的山峰
说明：4和8都是峰值元素，返回4的索引1或者8的索引5都可以
"""

def solution(nums: list)->int:
    left = 0
    right = 1
    while left < right:
        mid = (left+right) // 2
        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid + 1
    return right

print(solution([3,6]))