class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if nums==[]:
            return 1
        for i in range(len(nums)):
            if nums[i]>=1:
                nums = nums[i:]
                break
        nums = sorted(list(set(nums)))
        for i in range(len(nums)):
            if not nums[i] == i+1:
                return i+1
        return len(nums)+1




u = Solution()
test = [
    [1,2,0],
    [3,4,-1,1],
    [2],
    [0,-1,3,1],
    [0,2,2,1,1],
    [1,10000]


]
for x in test:
    print(u.firstMissingPositive(x))
