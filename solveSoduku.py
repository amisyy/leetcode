class Solution(object):
    def row_check(self,board,value,i,j):
        return value not in board[i]
    def col_check(self,board,value,i,j):
        zip_board = [board[v][j] for v in range(9)]

        return value not in zip_board
    def block_check(self,board,value,i,j):
        block_i = i//3
        block_j = j//3
        block = [board[m][n] for m in range(block_i*3,block_i*3+3) for n in range(block_j*3,block_j*3+3)]
        return value not in block
    def check_all(self,board,value,i,j):
        return self.block_check(board,value,i,j) and self.col_check(board,value,i,j) and self.row_check(board,value,i,j)
    def start_point(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    return i,j
        return i,j
    def recusion_search(self,board):
        i,j = self.start_point(board)
        if i>=8 and j>=8 and not board[i][j]==".":
            return True
        for value in range(1,10):
            if self.check_all(board,str(value),i,j):
                board[i][j] = str(value)
                if not self.recusion_search(board):
                    board[i][j] =  "."
                else:
                    return True
        return False
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.recusion_search(board)
        print(board)




u = Solution()
test = [
    [['8','.','.','.','.','.','.','.','.'],
     ['.','.','3','6','.','.','.','.','.'],
     ['.','7','.','.','9','.','2','.','.'],
     ['.','5','.','.','.','7','.','.','.'],
     ['.','.','.','.','4','5','7','.','.'],
     ['.','.','.','1','.','.','.','3','.'],
     ['.','.','1','.','.','.','.','6','8'],
     ['.','.','8','5','.','.','.','1','.'],
     ['.','9','.','.','.','.','.','4','.']],
[[".",".","9","7","4","8",".",".","."],
 ["7",".",".",".",".",".",".",".","."],
 [".","2",".","1",".","9",".",".","."],
 [".",".","7",".",".",".","2","4","."],
 [".","6","4",".","1",".","5","9","."],
 [".","9","8",".",".",".","3",".","."],
 [".",".",".","8",".","3",".","2","."],
 [".",".",".",".",".",".",".",".","6"],
 [".",".",".","2","7","5","9",".","."]]


]
for x in test:
    u.solveSudoku(x)
