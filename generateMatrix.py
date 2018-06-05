class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        multilist = [[0 for col in range(n)] for row in range(n)]
        num = 1
        i = 0
        j = 0
        max = n - 1
        min = 0
        while num<=n**2:
            multilist[i][j] = num
            if i == min and j < max:
                j += 1
            elif j == max and i < max:
                i += 1
            elif i == max and j > min:
                j -= 1
            elif j == min and i > min:
                if i == min + 1:
                    min += 1
                    max -= 1
                    j += 1
                else:
                    i -= 1
            num += 1
        return multilist



u = Solution()

test = [
3,4,5,1,2


]


for x in test:
    print(u.generateMatrix(x))


