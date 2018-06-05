class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length<=1:
            return [nums]
        result = []
        for i in range(length):
            if i>0:
                if nums[i] == nums[i-1]:
                    continue
            for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                if isinstance(j,int):
                    result.append([nums[i],j])
                else:
                    j.append(nums[i])
                    result.append(j)

        return result


u = Solution()
test = [
    [1,2],
    [1,2,3],
    [],
    [1],
    [5,4,6,2],
    [1,1,2]


]
for x in test:
    print(u.permuteUnique(x))
