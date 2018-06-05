class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[-1 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    result[i][j] = 0
                if i==0 or j==0:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i-1][j]+result[i][j-1]
        return result[m-1][n-1]




u = Solution()

test = [
    1
]
for x in test:
    print(u.uniquePaths(1,1))

