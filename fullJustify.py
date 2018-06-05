class Solution(object):
    def gap_words(self, word, maxWidth,last):
        length = len(word) - 1
        if last:
            result = ""
            result += word[0]
            res = maxWidth - word[-1]
            for i in range(length-1):
                result += " "
                result += word[i+1]
            result += res * " "
            return result
        if length == 1:
            return word[0] + ' ' * (maxWidth - len(word[0]))
        gap_res = (maxWidth - word[-1]) % (length - 1)
        gap = (maxWidth - word[-1]) // (length - 1) + 1
        result = ""
        result += word[0]
        for i in range(length-1):
            if gap_res > 0:
                result += " " * (gap + 1)
                result += word[i+1]
                gap_res -= 1
            else:
                result += " " * gap
                result += word[i+1]
        return result
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        words_bag = []
        temp = []
        temp_length = 0
        for i in words:
            if temp_length==0:
                temp_length += len(i)
                temp.append(i)
                continue
            else:
                if temp_length + 1 + len(i) <= maxWidth:
                    temp_length = temp_length + 1 + len(i)
                    temp.append(i)
                else:
                    temp.append(temp_length)
                    words_bag.append(temp)
                    temp = []
                    temp.append(i)
                    temp_length = len(i)
        temp.append(temp_length)
        words_bag.append(temp)
        result = []
        for i in range(len(words_bag) - 1):
            result.append(self.gap_words(words_bag[i], maxWidth, False))
        result.append(self.gap_words(words_bag[-1], maxWidth, True))
        return result




u = Solution()

test = [
    1
]
for x in test:
    print(u.fullJustify(["What","must","be","shall","be."],12))



