class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def helper(row, col):
            if row == len(matrix) - 1 or col == len(matrix[0]) - 1:
                return True
            new_r = row + 1
            new_c = col + 1
            if 0 <= new_r < len(matrix) and \
            0 <= new_c < len(matrix[row]):
                
                if matrix[row][col] == matrix[new_r][new_c]:
                    
                    res = helper(new_r, new_c)
                else:
                    res = False
                    return res
            
            return res
        lst = []
        for row in range(len(matrix) - 1):
            for col in range(len(matrix[0]) - 1):
                if row == 0:
                    lst.append((row, col))
                elif col == 0:
                    lst.append((row, col))
                else:
                    break
        for i in lst:
            res = helper(i[0], i[1])
            if not res:
                return False
        return True
            