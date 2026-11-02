class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        med = sorted(nums)[len(nums)//2]
        return sum(abs(x-med) for x in nums)
     


                