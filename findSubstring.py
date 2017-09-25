class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_length = len(words[0])
        word_num = len(words)
        length = len(s)
        words_dict = {}
        for i in words:
            if i not in words_dict:
                words_dict[i] = 1
            else:
                words_dict[i]+=1
        res = []
        for i in range(length -word_length*word_num +1 ):
            dict_curr={}
            j=0
            while j < word_num:
                word = s[i+j*word_length:i+(j+1)*word_length]
                if word not in words_dict:
                    break
                elif word not in dict_curr:
                    dict_curr[word] = 1
                else:
                    dict_curr[word] +=1
                    if dict_curr[word] > words_dict[word]:
                        break
                j +=1
            if j==word_num:
                res.append(i)
        return res





u = Solution()
print(u.findSubstring("barfoothefoobarman",["foo","bar"]))
