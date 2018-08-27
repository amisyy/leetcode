class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return 0
        else:
            div_list = []
            left = 2
            right = n
            mod = n
            while left <= right and mod >= left:
                while mod % left == 0 and mod >= left:
                    div_list.append(left)
                    mod /= left
                left += 1
            ret = 0
            for i in div_list:
                ret += i
            return ret


u = Solution()
print(u.minSteps(9))


