class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            vals = [c for c in r if c != '.']
            if len(set(vals)) != len(vals):
                return False

        for i in range(9):
            vals.clear()
            for j in range(9):
                if board[j][i] != '.':
                    vals.append(board[j][i])

                if len(set(vals)) != len(vals):
                    return False

        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                vals.clear()
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if board[i+di][j+dj] != '.':
                            vals.append(board[i+di][j+dj])
                            
                        if len(set(vals)) != len(vals):
                            return False

        return True