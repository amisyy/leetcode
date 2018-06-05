class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if not len1+len2==len3:
            return False
        flag = [[False for i in range(len2+1)]for j in range(len1+1)]
        flag[0][0] = True
        for i in range(len1):
            flag[i+1][0] = flag[i][0] and s1[i] == s3[i]
        for i in range(len2):
            flag[0][i+1] = flag[0][i] and s2[i] == s3[i]
        for i in range(len1):
            for j in range(len2):
                flag[i+1][j+1] = (flag[i][j+1] and s1[i] == s3[i+j+1]) or (flag[i+1][j] and s2[j] == s3[i+1+j])
        return flag[len1][len2]


u = Solution()



test = [
1
]

for x in test:
    print(u.isInterleave("aa","ab","abaa"))




