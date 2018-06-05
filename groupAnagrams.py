class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group={}
        for i in strs:
            group.setdefault(tuple(sorted(i)),[]).append(i)
        return group.values()


u = Solution()
test = [
    ["eat", "tea", "tan", "ate", "nat", "bat"]


]
print(tuple("eat"))
print(tuple("ate"))
for x in test:
    print(u.groupAnagrams(x))
