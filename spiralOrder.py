class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==[[]]:
            return []
        row = len(matrix)
        col = len(matrix[0])

        a = [matrix[0][i] for i in range(col)]

        b = [matrix[i+1][col-1] for i in range(row-1)] if row>1 else []

        c = [matrix[row-1][col-i-2] for i in range(col-1)] if col>1 and row>1 else []
        d = [matrix[row-i-2][0] for i in range(row-2)] if row>2 and col>1 else []
        a.extend(b)
        a.extend(c)
        a.extend(d)
        e = self.spiralOrder([matrix[1:row-1][i][1:col-1] for i in range(row-2)]) if (row > 2 and col > 2)  else []

        a.extend(e)
        return a



u = Solution()
test = [

[[1, 2], [4, 5], [7, 8]],
    [[]],
    [[1]],
    [[1,2,3],[4,5,6],[7,8,9]],
    [[2,3]]


]


a = [[1,2,3,4],[4,5,6,7],[7,8,9,9],[10,11,12,13]]
b = [4,5,6]
print([a[1:3][i][1:3] for i in range(3-1)])
for x in test:
    print(u.spiralOrder(x))

