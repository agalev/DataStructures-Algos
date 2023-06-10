# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(prices: list) -> int:
    profit = 0
    min = prices[0]
    for i in range(len(prices)):
        if prices[i] < min:
            min = prices[i]
        elif profit < prices[i] - min:
            profit = prices[i] - min
    print(profit)
    return profit

maxProfit([7,1,5,3,6,4]) # 5