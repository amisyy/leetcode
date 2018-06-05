class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num0 = 0
        num1 = 0
        num2 = 0
        for i in nums:
            if i==0:
                num0 += 1
            elif i==1:
                num1 += 1
            else:
                num2 += 1
        nums = num0*[0]+num1*[1]+num2*[2]
        return nums

u = Solution()

test = [
1
]
for x in test:
    print(u.sortColors([1,1,1,0,0,0,2,2,2]))




