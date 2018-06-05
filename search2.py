class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        #(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
        n = len(nums)
        lo = 0
        hi = n-1

        while lo<=hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[hi]:
                if nums[mid]>target and nums[lo]<=target:
                    hi = mid
                else:
                    lo = mid + 1
            elif nums[mid] < nums[hi]:
                if nums[mid]< target and nums[hi]>=target:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                hi -= 1
        return nums[lo] == target

u = Solution()

test = [
    1
]
for x in test:
    print(u.search([4 ,5 ,6 ,7, 0, 1, 2],2))




