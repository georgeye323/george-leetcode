#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""--------------------------------------------------------------------------
@FileName:		3、两数之和.py
@Author:		叶畈
@Version:		v1.0.0
@CreationDate:	2024/2/20 15:18
@Update Date:	2024/2/20 15:18
@Description:

--------------------------------------------------------------------------"""
nums = [3, 3]
targets = 6


def solution():
    valToIndex = {}
    for i in range(len(nums)):
        # 查表，看看是否有能和 nums[i] 凑出 target 的元素
        need = targets - nums[i]
        if need in valToIndex:
            return [valToIndex[need], i]
        # 存入 val -> index 的映射
        valToIndex[nums[i]] = i


ret = solution()
print(ret)
