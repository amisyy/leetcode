class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_area = 0
        row = len(matrix)
        length = len(matrix[0])
        height = [[0 for i in range(length)] for j in range(row)]
        for i in range(row):
            stack = [-1]
            height[i].append(0)
            matrix[i].append('0')
            for j in range(length+1):
                if i ==0:
                    height[i][j] = int(matrix[i][j])
                else:
                    height[i][j] = 0 if matrix[i][j] == '0' else height[i-1][j] + 1
                while height[i][j] < height[i][stack[-1]]:
                    h = height[i][stack.pop()]
                    w = j - stack[-1] - 1
                    max_area = max(max_area,h*w)
                stack.append(j)
        return max_area

u = Solution()



test = [
[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
]
for x in test:
    print(u.maximalRectangle(x))




