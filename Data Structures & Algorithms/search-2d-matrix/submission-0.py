class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        smallRow = 0
        bigRow = rows - 1

        #find row:
        while smallRow <= bigRow:
            curRow = (smallRow + bigRow) // 2
            if target > matrix[curRow][-1]:
                smallRow = curRow + 1
            elif target < matrix[curRow][0]:
                bigRow = curRow - 1
            else:
                break
        
        if not smallRow <= bigRow:
            return False
        
        smallCol = 0
        bigCol = cols - 1

        while smallCol <= bigCol:
            curCol = (smallCol + bigCol) // 2
            if target > matrix[curRow][curCol]:
                smallCol = curCol + 1
            elif target < matrix[curRow][curCol]:
                bigCol = curCol - 1
            else:
                break
        
        if not smallCol <= bigCol:
            return False
        
        return True