class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        zip_board = [[r[col] for r in board] for col in range(len(board[0]))]
        block = ["","","","","","","","",""]
        for i in range(9):
            for j in range(9):
                block_i = i//3
                block_j = j//3
                block[block_i*3+block_j] += board[i][j]

        for i in range(9):
            for j in range(9):
                count_b = board[j].count(str(i+1))
                count_z = zip_board[j].count(str(i+1))
                count_bl = block[j].count(str(i+1))
                if count_b>1 or count_z>1 or count_bl>1:
                    return False

        return True








u = Solution()
test = [
    [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"],
[".........",".........",".9......1","8........",".99357...",".......4.","...8.....",".1....4.9","...5.4..."]
]
for x in test:
    print(u.isValidSudoku(x))
