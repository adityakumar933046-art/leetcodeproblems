class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, total, path):

            if total == target:
                ans.append(path[:])
                return

            if i == len(candidates) or total > target:
                return

            # take current number
            path.append(candidates[i])
            dfs(i, total + candidates[i], path)

            path.pop()
            dfs(i + 1, total, path)

        dfs(0, 0, [])

        return ans