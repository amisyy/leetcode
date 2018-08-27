class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                diff = prices[i + 1] - prices[i]
                profit += diff
        return profit


u = Solution()
test = [
    [7, 1, 5, 3, 6, 4],
    [1, 2, 3, 4, 5],
    [7, 6, 4, 3, 1]

]
for i in test:
    print(u.maxProfit(i))