class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,i,j,word):
                    return True
        return False
    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


u = Solution()

test = [
1
]
for x in test:
    print(u.exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']],"SEE"))



