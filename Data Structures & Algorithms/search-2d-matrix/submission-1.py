class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #use binary serach to find which 2 cols or rows its between then use binart search within the remaining cooridnate
        row_p1 = 0
        row_p2 = len(matrix) - 1

        col_p1 = 0
        col_p2 = len(matrix[0]) - 1
        while (row_p1 <= row_p2) :#row outside then col inside for faster bc memory
            row_mid = row_p1 + (row_p2 - row_p1) // 2
            if (target >= matrix[row_mid][col_p1] ) and (target <= matrix[row_mid][col_p2]): #its within the range of this row
                while (col_p1 <= col_p2):
                    col_mid = col_p1 + (col_p2 - col_p1) // 2
                    if matrix[row_mid][col_mid] == target: return True
                    elif target > matrix[row_mid][col_mid]:
                        col_p1 = col_mid + 1
                    else:
                        col_p2 = col_mid - 1
            elif target > matrix[row_mid][col_p2]:
                row_p1 = row_mid + 1
            else:
                row_p2 = row_mid - 1
        return False



                    

        