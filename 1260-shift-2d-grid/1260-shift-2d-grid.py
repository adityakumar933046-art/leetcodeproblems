class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        total = m * n

        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                old = i * n + j
                new = (old + k) % total

                r = new // n
                c = new % n

                ans[r][c] = grid[i][j]

        return ans