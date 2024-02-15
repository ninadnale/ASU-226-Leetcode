class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        longest = 0

        def dfs(i, j, prev):
            if(i<0 or j<0 or i>=ROWS or j>=COLS or matrix[i][j]<=prev):
                return 0
            if((i,j) in cache):
                return cache[(i,j)]
            
            res = 1
            res = max(res, 1 + dfs(i+1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j+1, matrix[i][j]))
            res = max(res, 1 + dfs(i-1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j-1, matrix[i][j]))

            cache[(i,j)] = res
            return res

        for i in range(ROWS):
            for j in range(COLS):
                longest = max(longest, dfs(i, j, -1))

        return longest