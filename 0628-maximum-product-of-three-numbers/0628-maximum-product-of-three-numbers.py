class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        c = sorted(nums)
        a= c[-2]*c[-1]*c[-3]
        b = c[0]*c[1]*c[-1]
        return max(a,b)
