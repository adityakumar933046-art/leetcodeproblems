class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return piles[i]

            left = piles[i] - dfs(i + 1, j)
            right = piles[j] - dfs(i, j - 1)

            return max(left, right)

        return dfs(0, len(piles) - 1) > 0