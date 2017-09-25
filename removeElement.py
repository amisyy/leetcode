class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        j = 0
        for i in range(length):
            if nums[i] == val:
                continue
            nums[j] = nums[i]
            j+=1
        return j



u = Solution()
print(u.hasCycle(n1))
