class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n==2:
            return 2
        else:
            result = [1,2]
            for i in range(n-2):
                result.append(result[i] + result[i+1])
            return result[-1]


u = Solution()

test = [
    1
]
for x in test:
    print(u.climbStairs(35))



