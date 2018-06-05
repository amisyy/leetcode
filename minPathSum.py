class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        result = [[-1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    result[i][j] = grid[i][j]
                elif i==0 and j>0:
                    result[i][j] =  result[i][j-1] + grid[i][j]
                elif j==0 and i>0:
                    result[i][j] = result[i-1][j] + grid[i][j]
                else:
                    result[i][j] = min(result[i][j-1] , result[i-1][j]) + grid[i][j]
        return result[m-1][n-1]


u = Solution()

test = [
    1
]
for x in test:
    print(u.minPathSum([[1,3,1],
 [1,5,1],
 [4,2,1]]))



