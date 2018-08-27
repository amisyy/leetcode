class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = {}
        for i in nums:
            times[i] = 0
        for i in times:
            times[i] += 1
        for i in times.keys():
            if times[i] == 1:
                return i