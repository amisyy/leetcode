class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in nums:
            ret = i ^ ret
        return ret
u = Solution()
print(u.singleNumber([4,1,2,1,2]))
