class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right  = 0
        right_reg = 0
        left = len(nums) - 1
        left_reg = left
        right_sum = left_sum = 0
        while right<left:
            right_sum += nums[right]
            left_sum += nums[left]
            right += 1
            left-=1
            if right_sum<0:

                right_reg = right
                right_sum = 0
            if left_sum < 0:
                left_reg = left
                left_sum = 0
        if left_reg+1<=right_reg:
            return max(nums)
        return max(sum(nums[right_reg:left_reg+1]),max(nums))


u = Solution()
test = [

     [-1, 2, 2, -3],[1, -1, -2],[-2, 1, -3, 4, -1, 2, 1, -5, 4],    [-2,1],[1,-1],[-1,-2]


]

for x in test:
    print(u.maxSubArray(x))
