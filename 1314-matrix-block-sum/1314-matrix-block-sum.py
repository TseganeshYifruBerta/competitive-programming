class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
		
		# Calculate the prefix sum
        prefix_sum = mat.copy()
        print(prefix_sum)
        
#         prefix sum for the matrix
        for row in range(rows):
            for col in range(cols):
                if row > 0:
                    prefix_sum[row][col] += prefix_sum[row - 1][col]
                    
                if col > 0:
                    prefix_sum[row][col] += prefix_sum[row][col - 1]
                    
                if row > 0 and col > 0:
                    prefix_sum[row][col] -= prefix_sum[row - 1][col - 1]
                    
                    
        print(prefix_sum)
		# using the prefix calculate the blocksum
        blocksum = [[0 for i in range(cols)] for j in range(rows)]
        for row in range(rows):
            for col in range(cols):
                
                blocksum[row][col] += prefix_sum[min(rows - 1 ,row + k)][min(col + k, cols - 1)]
                
                if col - k > 0 and row - k  > 0:
                    blocksum[row][col] += prefix_sum[row - k - 1][col - k - 1]
                    
                if row - k > 0:
                    blocksum[row][col] -= prefix_sum[row - k - 1][min(col + k, cols - 1)]
                    
                if col - k > 0:
                    blocksum[row][col] -= prefix_sum[min(row + k, rows - 1)][col - k - 1]
                    
        return blocksum
    