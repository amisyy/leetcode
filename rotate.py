class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        temp = [[[matrix[-r - 1][col] for r in range(len(matrix))] for col in range(len(matrix[0]))]]

        matrix.clear()

        return matrix

u = Solution()
test = [
    [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]


]
for x in test:
    print(u.rotate(x))
