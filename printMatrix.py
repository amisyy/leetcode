# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix[0]:
            return []
        ret = []
        # heng
        for i in range(len(matrix[0])):
            ret.append(matrix[0][i])
        # shu
        if len(matrix) >= 2:
            for i in range(1, len(matrix)):
                ret.append(matrix[i][-1])
        else:
            return ret
        # heng
        if len(matrix[0]) >= 2:
            for i in range(1, len(matrix[0])):
                ret.append(matrix[-1][len(matrix[0]) - i - 1])
        # shu
        if len(matrix) >= 3 and len(matrix[0])>=2:
            for i in range(1, len(matrix) - 1):
                ret.append(matrix[len(matrix) - i - 1][0])

        if len(matrix) >= 3 and len(matrix[0]) >= 3:
            new_matrix = [[i for i in matrix[j][1:len(matrix[0]) - 1]] for j in range(1, len(matrix) - 1)]
            next_ret = self.printMatrix(new_matrix)
            ret = ret + next_ret
            return ret
        else:
            return ret


u = Solution()
print(u.printMatrix([[1],[2],[3],[4],[5]]))
# [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
