class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        p = 0
        while p < len(matrix):
            t = []
            for i in range(len(matrix)):
                t.append(matrix[i][p])
            t.reverse()
            temp.append(t)
            p += 1
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                matrix[row][col] = temp[row][col]
        