class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profit = 0
        # cur_min = prices[0]
        #
        # for i in prices:
        #     profit = max(profit, i - cur_min)
        #     cur_min = min(i, cur_min)
        # return profit
        length = len(prices)
        if length < 2:
            return 0
        preprofit = [0]
        precurmin = prices[0]
        profit_sum = 0
        for i in range(1,length):
            preprofit.append(max(preprofit[-1], prices[i] - precurmin))
            precurmin = min(precurmin, prices[i])
        backprofit = [0]
        backcurmax = prices[-1]
        for i in range(1,length):
            backprofit.append(max(backprofit[-1],backcurmax-prices[length-1-i]))
            backcurmax = max(backcurmax,prices[length-1-i])
        print(preprofit)
        print(backprofit)
        for i in range(length):
            profit_sum = max(profit_sum,preprofit[i]+backprofit[length-i-1])
        return profit_sum


tests = [
    [3, 3, 5, 0, 0, 3, 1, 4],
    [1, 2, 3, 4, 5],
    [7, 6, 4, 3, 1]

]
u = Solution()
for test in tests:
    print(u.maxProfit(test))
