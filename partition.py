class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        length = len(s)
        is_rotate = [[1 if i == j else 0 for i in range(length)] for j in range(length)]
        ret = []
        for i in range(length):
            left = i - 1
            if left >= 0 and s[left] == s[i]:
                is_rotate[left][i] = 1
            right = i + 1
            if right <= length - 1 and s[i] == s[right]:
                is_rotate[i][right] = 1
            while left >= 0 and right <= length - 1:
                if left >= 1:
                    is_rotate[left - 1][right] = 1 if is_rotate[left][right - 1] == 1 and s[left - 1] == s[right] else \
                        is_rotate[left - 1][right]
                if right + 1 <= length - 1:
                    is_rotate[left][right + 1] = 1 if is_rotate[left + 1][right] == 1 and s[left] == s[right + 1] else \
                    is_rotate[left][right + 1]
                is_rotate[left][right] = 1 if is_rotate[left + 1][right - 1] == 1 and s[left] == s[right] else \
                    is_rotate[left][right]
                left -= 1
                right += 1
        print(is_rotate)
        return self.huiwen([], 0, s, [], is_rotate)

    def huiwen(self, tmp, index, s, result, is_rotate):
        if index == len(s):
            result.append(tmp)
        else:
            for i in range(index, len(s)):
                if is_rotate[index][i]:
                    result = self.huiwen(tmp + [s[index:i + 1]], i + 1, s, result, is_rotate)
        return result


u = Solution()
print(u.partition('abbab'))
