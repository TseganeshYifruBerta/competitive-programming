class Solution:
    def countBattleship(self, row, col, visited, matrix):
        visited.add((row,col))
        vertical = False

        new_row = row + 1
        while new_row < len(matrix) and matrix[new_row][col] == 'X' and (new_row, col) not in visited:
            vertical = True
            visited.add((new_row, col))
            new_row += 1

        if vertical:
            return visited

        new_col = col + 1
        while new_col < len(matrix[0]) and matrix[row][new_col] == 'X' and (row, new_col) not in visited:
            visited.add((row, new_col))
            new_col += 1

        return visited
        
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        answer = 0
        matrix = board
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 'X' and (row, col) not in visited:
                    visited = self.countBattleship(row, col, visited, matrix)
                    answer += 1

        return answer