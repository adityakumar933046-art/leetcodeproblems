class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a= sorted(nums)
        b = (a[-1]-1)*(a[-2]-1)
        return b
        