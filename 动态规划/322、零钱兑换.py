"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

"""
# class Solution:
#     # TODO leetcode超出时间限制
#     import functools
#     def coinChange(self, coins: List[int], amount: int) -> int:
#
#         def dp(rem: int) -> int:
#             if rem == 0:
#                 return 0
#             if rem < 0:
#                 return -1
#             res = float('inf')
#             for i in coins:
#                 subProblem = dp(rem-i)
#                 if subProblem >= 0 and subProblem < res:
#                     res = subProblem + 1
#             return res if res < float('inf') else -1
#         if amount < 1:
#             return 0
#         return dp(amount)
#
#     def coinChange2(self, coins: list[int], amount: int) -> int:
#         memo = [-1]*(amount+1)
#
#         def helper(coins: list[int], amount: int) -> int:
#             # 带备忘录
#             if amount == 0:
#                 return 0
#             if amount < 0:
#                 return -1
#             if memo[amount] != -1:
#                 return memo[amount]
#             res = float('inf')
#             for i in coins:
#                 subProblem = self.coinChange(coins, amount - i)
#                 if subProblem == -1:
#                     # 计算子问题无解 跳过
#                     continue
#                 res = min(res, subProblem + 1)
#             # 把计算结果存入到备忘录
#             memo[amount] =  -1 if res == float('inf') else res
#             return memo[amount]
#
#         return helper(coins, amount)

from typing import List
from functools import lru_cache

class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache()
        def dp(rem) -> int:
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            mini = int(1e9)
            for coin in coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1
        if amount < 1:
            return 0
        return dp(amount)


if __name__ == "__main__":
    test = Solution1()
    result = test.coinChange([186,419,83,408], 6249)
    print(result)