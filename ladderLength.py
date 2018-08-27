class Solution:
    def ladderLength2(self, beginWords, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList or endWord not in wordList:
            return 0
        next_beginWords = []
        next_wordList = []
        for word in beginWords:
            for word_in_list in wordList:
                if self.compare(word,word_in_list):
                    if word_in_list == endWord:
                        return 1
                    else:
                        next_beginWords.append(word_in_list)
                next_wordList.append(word_in_list)
        if not next_beginWords:
            return 0
        result = self.ladderLength2(next_beginWords,endWord,next_wordList)
        if result:
            return 1 + result
        else:
            return 0

    def ladderLength(self, beginWord, endWord, wordList):
        if not wordList or endWord not in wordList:
            return 0
        result = self.ladderLength2([beginWord],endWord,wordList)
        if result:
            return 1 + result
        else:
            return 0
    def compare(self,a_word,b_word):
        diff = 0
        for i in range(len(a_word)):
            if not a_word[i] == b_word[i]:
                diff += 1
                if diff > 1:
                    return False
        if diff == 0:
            return False
        return True
u = Solution()
print(u.ladderLength("hot","dog",["hot","dog"]))
    #

    #"hit","cog", ["hot","dot","dog","lot","log","cog"]))
