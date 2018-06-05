class Solution(object):
    def nextPermutation(self, nums):

        length = len(nums)
        i = length-1

        while i > 0:
            if nums[i] >nums[i-1]:
                swift = nums[i-1]
                break
            i-=1
        if i==0:
            nums =  sorted(nums)
        else:
            min = nums[i]
            min_index = i
            j = i + 1
            while j <= length-1:
                if min > nums[j] and nums[j]>nums[i-1]:
                    min = nums[j]
                    min_index = j
                j+=1
            temp = nums[i-1]
            nums[i-1] = nums[min_index]
            nums[min_index] = temp
            nums[i:] = sorted(nums[i:])
        return nums



u = Solution()
print(u.nextPermutation([3,2,1]))
