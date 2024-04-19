class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if(not grid):
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def bfs(r, c):
            que = deque()
            visited.add((r,c))
            que.append((r,c))

            while que:
                row, col = que.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if(r in range(ROWS) and c in range(COLS) and grid[r][c]=='1' and (r,c) not in visited):
                        que.append((r,c))
                        visited.add((r,c))

        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j]=='1' and (i,j) not in visited):
                    bfs(i,j)
                    num_islands += 1
        
        return num_islands

         

        