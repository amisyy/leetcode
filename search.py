class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        low = 0
        high = length-1
        while low<high:
            mid = (low+high)//2
            if (target>nums[mid] and nums[mid]>=nums[0])or(target>nums[mid]and target<=nums[length-1])or (target<nums[mid] and nums[mid]>=nums[0]and target<nums[0]):
                low = mid+1
            else:
                high = mid

        return  low if target in nums[low:low+1] else -1



u = Solution()
print(u.search([5,1,3],3))
