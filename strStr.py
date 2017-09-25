class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return 0
        h = len(haystack)
        n = len(needle)
        if h < n:
            return -1
        for i in range(h-n+1):
            for j in range(n):
                if not haystack[i+j]==needle[j]:
                    break
            if j==n-1:
                return i
        return -1



u = Solution()
print(u.strStr("abcde","abc"))
