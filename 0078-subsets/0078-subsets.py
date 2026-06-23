class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for x in nums:
            ans += [s + [x] for s in ans]

        return ans