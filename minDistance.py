class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #d[i][0] = d[0][i]=i一个只需要做i次删除，一个只需要做i次插入
        #d[i][j] = d[i-1][j] + 1 d[i][j] = d[i][j-1]+1
        #如果word[i-1] = word[j-1] 那么d[i][j] = d[i-1][j-1] 否则那么d[i][j] = d[i-1][j-1]+1
        m = len(word1) + 1
        n = len(word2) + 1
        d = [ [0 for i in range(n)] for j in range(m) ]
        for i in range(m):
            d[i][0] = i
        for j in range(n):
            d[0][j] = j
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + (1 if word1[i-1]==word2[j-1] else 0))
        return d[m-1][n-1]



u = Solution()

test = [
1
]
for x in test:
    print(u.minDistance("a","a"))




