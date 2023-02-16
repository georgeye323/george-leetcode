# dp[i][j]的含义表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。
"""
    不放物品i：
        由dp[i - 1][j]推出，即背包容量为j，里面不放物品i的最大价值，此时dp[i][j]就是dp[i - 1][j]。
        (其实就是当物品i的重量大于背包j的重量时，物品i无法放进背包中，所以被背包内的价值依然和前面相同。)
"""
"""
     放物品i：
        由dp[i - 1][j - weight[i]]推出，dp[i - 1][j - weight[i]] 为背包容量为j - weight[i]的时候不放物品i的最大价值，
        那么dp[i - 1][j - weight[i]] + value[i] （物品i的价值），就是背包放物品i得到的最大价值
"""
"""
    有n件物品和一个最多能背重量为w 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。
    每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
"""
def test2_wei_bag_problem(bag_size: int, weight: list, value: list)->int:
    rows, cols = len(weight), bag_size + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # 初始化數組
    for i in range(rows):
        dp[i][0] = 0
    first_item_weight, first_item_value = weight[0], value[0]
    for j in range(1, cols):
        if first_item_weight <= j:
            dp[0][j] = first_item_value

    # 更新dp數組，先遍歷物品，再遍歷背包
    for i in range(1, len(weight)):
        cur_weight, cur_val = weight[i], value[i]
        for j in range(1, cols):
            if cur_weight > j:
                # 説明背包裝不下當前物品
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cur_weight]+cur_val)
    print(dp)



if __name__ == "__main__":
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    test2_wei_bag_problem(bag_size, weight, value)
