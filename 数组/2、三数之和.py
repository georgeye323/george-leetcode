#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""--------------------------------------------------------------------------
@FileName:		2、三数之和.py
@Author:		叶畈
@Version:		v1.0.0
@CreationDate:	2024/2/22 17:59
@Update Date:	2024/2/22 17:59
@Description:	leetcode三数之和--双指针办法
--------------------------------------------------------------------------"""
def three_sums(nums):
    sorted_nums = sorted(nums)
    result = []
    for i in range(len(sorted_nums)-2):
        if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
            continue
        left = i + 1
        right = len(sorted_nums) - 1
        while left < right:
            total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            if total == 0:
                result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                # 跳过重复的元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    print(result)


three_sums([-1,0,1,2,-1,-4])