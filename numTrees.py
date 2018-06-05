class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            count = [0 for i in range(n+1)]
            count[0] = count[1] = 1
            for i in range(n-1):
                for j in range(i+2):
                    count[i+2] += count[j]*count[i+1-j]
            return count[-1]


u = Solution()



test = [
1,2,3,4
]

for x in test:
    print(u.numTrees(x))




