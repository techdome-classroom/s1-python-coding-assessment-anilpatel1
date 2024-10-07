class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
                    if not map:
            return 0

        rows = len(map)
        cols = len(map[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or map[r][c] == 'W' or visited[r][c]:
                return
            visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        island_count = 0

        for i in range(rows):
            for j in range(cols):
                if map[i][j] == 'L' and not visited[i][j]:
                    island_count += 1
                    dfs(i, j)

        return island_count
