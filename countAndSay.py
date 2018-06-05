class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_set = []
        length = len(candidates)
        candidates = sorted(candidates)
        for i in range(length):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                continue
            elif candidates[i] == target:
                result_set.append([candidates[i]])
            elif i<length-1:
                temp = self.combinationSum2(candidates[i+1:],target-candidates[i])
                if not temp == []:
                    for j in temp:
                        j.append(candidates[i])
                        result_set.append(j)
        return result_set


u = Solution()
test = [
1
]
for x in test:
    print(u.combinationSum2([8,8],8))
