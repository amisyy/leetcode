class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations
        length = len(nums)
        com_list = []
        for i in range(length):

            com_list.append(list(combinations(nums, i)))
        return com_list

u = Solution()

test = [
1
]
for x in test:
    print(u.subsets([1,2,3]))




