class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        j = 0
        length = len(nums)
        if length==0:
            return 0
        for i in range(length)-1:
            if not nums[j]==nums[i+1]:
                j+=1
                nums[j] = nums[i+1]
        return j+1


u = Solution()
print(u.hasCycle(n1))
