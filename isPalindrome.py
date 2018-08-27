class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = []
        for char in s:
            if char.isalpha() or char.isdigit():
                new_s.append(char.lower())
        length = len(new_s)
        half_length = length // 2

        for i in range(half_length):
            if not new_s[i] == new_s[length - 1 - i]:
                return False
        return True


u = Solution()
test = [
    "A man, a plan, a canal: Panama",
    "race a car"
]
for i in test:
    print(u.isPalindrome(i))
