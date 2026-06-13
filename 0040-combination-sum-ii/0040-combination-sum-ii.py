class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def backtrack(start, target, path):

            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                backtrack(i + 1, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])

        return res