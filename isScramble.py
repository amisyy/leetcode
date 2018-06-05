class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1==s2:
            return True
        if not len(s1) == len(s2) or not sorted(s1) == sorted(s2):
            return False

        for i in range(len(s1)-1):
            s11 = s1[:i+1]
            s12 = s1[i+1:]
            s21 = s2[:i+1]
            s22 = s2[i+1:]
            if self.isScramble(s11,s21) and self.isScramble(s12,s22):
                return True
            s21 = s2[len(s1)-i-1:]
            s22 = s2[:len(s1)-i-1]
            if self.isScramble(s11,s21) and self.isScramble(s12,s22):
                return True
        return False


u = Solution()



test = [
1
]
for x in test:
    print(u.isScramble('great','rgtae'))




