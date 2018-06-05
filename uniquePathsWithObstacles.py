class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[-1 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    result[i][j] = 0
                elif i == 0 or j == 0:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i - 1][j] + result[i][j - 1]
        return result[m - 1][n - 1]


u = Solution()

test = [
    1
]
for x in test:
    print(u.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))

