


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s.strip()
        for i in s:
            if i==" ":
                count=0
            else:
                count+=1
        return count


u = Solution()

test = [
"Hello World"


]


for x in test:
    print(u.lengthOfLastWord(x))


