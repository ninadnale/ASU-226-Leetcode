class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        memo = {}

        def dfs(r, c1, c2):
            if((r, c1, c2) in memo):
                return memo[(r, c1, c2)]
            if(c1==c2 or c1<0 or c2<0 or c1==COLS or c2==COLS):
                return 0
            if(r==ROWS-1):
                return grid[r][c1] + grid[r][c2]
            
            res = 0
            for c1_delta in [-1, 0, 1]:
                for c2_delta in [-1, 0, 1]:
                    res = max(res, 
                            dfs(r+1, c1+c1_delta, c2+c2_delta)+(grid[r][c1] + grid[r][c2]))
            
            memo[(r, c1, c2)] = res        

            return res
        
        return dfs(0, 0, COLS-1)