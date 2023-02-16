"""
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。
该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

    # TODO 优化1：利用数组形成备忘录

    def helper(self, memo: list, n: list) ->list:
        if n == 0 or n == 1:
            return n
        # 已经计算过了，不用计算
        if memo[n] != 0:
            return memo[n]
        memo[n] = self.helper(memo, n-1) + self.helper(memo, n-2)

    def fib2(self, n: int) -> int:
        # 初始化备忘录
        memo = [0] * (n+1)
        return  self.helper(memo, n)

    # TODO 优化2：由于F(n) = F(n - 1) + F(n - 2), 所以备忘录只需记录F(n - 1), F(n - 2)

    def fib3(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        memo_n_1 = 0
        memo_n_2 = 1
        for i in range(2, n+1):
            dp_i = memo_n_1 + memo_n_2
            # 滚动刷新
            memo_n_1 = memo_n_2
            memo_n_2 = dp_i
        return  memo_n_2

