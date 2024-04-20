class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        farms = []
        if(not land):
            return farms
        
        ROWS, COLS = len(land), len(land[0])
        visited = set()

        def bfs(r, c):
            que = deque()
            visited.add((r, c))
            que.append((r, c))
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            while que:
                row, col = que.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if(r in range(ROWS) and c in range(COLS) and (r,c) not in visited and land[r][c]==1):
                        que.append((r, c))
                        visited.add((r, c))
            
            return (row, col)

        for i in range(ROWS):
            for j in range(COLS):
                if(land[i][j]==1 and (i,j) not in visited):
                    temp = [i, j]
                    end_row, end_col = bfs(i, j)
                    temp.append(end_row)
                    temp.append(end_col)
                    farms.append(temp)
        
        return farms
