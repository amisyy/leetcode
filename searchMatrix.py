class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows*cols-1

        while low < high:
            mid = (low + high) // 2
            mid_num = matrix[mid // cols][mid % cols]

            if mid_num == target:
                return True
            elif mid_num< target:
                low = mid + 1
            else:
                high = mid -1
        if matrix[high // cols][high % cols] == target:
            return True
        return False


u = Solution()

test = [
1
]
for x in test:
    print(u.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))
if []:

    print(True)



