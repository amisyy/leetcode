class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) < 3:
            pass
        elif len(board[0]) < 3:
            pass
        else:
            change = [[0 if ((i == 0 or i == len(board[0]) - 1 or j == 0 or j == len(board) - 1) and board[j][
                i] == 'O') else 1 for i in
                       range(len(board[0]))] for j in range(len(board))]
            for i in range(1, min(len(board) // 2 + 2,len(board)-1)):
                for j in range(1, min(len(board[0]) // 2 + 2,len(board[0])-1)):
                    change[i][j] = 0 if (change[i - 1][j] == 0 or change[i][j - 1] == 0 or change[i + 1][j] == 0 or
                                         change[i][j + 1] == 0) and board[i][j] == 'O' else change[i][j]
                    i_ = len(board) - i - 1
                    j_ = len(board[0]) - j - 1
                    change[i_][j_] = 0 if (change[i_ - 1][j_] == 0 or change[i_][j_ - 1] == 0 or change[i_ + 1][
                        j_] == 0 or change[i_][j_ + 1] == 0) and board[i_][j_] == 'O' else change[i_][j_]
                    change[i][j] = 0 if (change[i - 1][j] == 0 or change[i][j - 1] == 0 or change[i + 1][j] == 0 or
                                         change[i][j + 1] == 0) and board[i][j] == 'O' else change[i][j]
            print(change)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if change[i][j] == 1 and board[i][j] == 'O':
                        board[i][j] = 'X'
            return board


board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
]
board2 = [
    ["O", "X", "X", "O", "X"],
    ["X", "O", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"]]
board3 = [["O", "O", "O", "O", "X", "X"],
          ["O", "O", "O", "O", "O", "O"],
          ["O", "X", "O", "X", "O", "O"],
          ["O", "X", "O", "O", "X", "O"],
          ["O", "X", "O", "X", "O", "O"],
          ["O", "X", "O", "O", "O", "O"]]
board4 = [["O","X","O","O","O","O","O","O","O"],
          ["O","O","O","X","O","O","O","O","X"],
          ["O","X","O","X","O","O","O","O","X"],
          ["O","O","O","O","X","O","O","O","O"],
          ["X","O","O","O","O","O","O","O","X"],
          ["X","X","O","O","X","O","X","O","X"],
          ["O","O","O","X","O","O","O","O","O"],
          ["O","O","O","X","O","O","O","O","O"],
          ["O","O","O","O","O","X","X","O","O"]]
u = Solution()
print(u.solve(board4))
