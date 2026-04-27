class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for index in range(9):
            
            rows = []
            row = board[index]
            for item in row:
                if item in rows:
                    return False
                else:
                    if item != ".":
                        rows.append(item)
            
            columns = []
            for row in board:
                if row[index] in columns:
                    return False
                else:
                    if row[index] != ".":
                        columns.append(row[index])
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True