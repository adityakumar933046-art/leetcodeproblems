from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums),max(nums)
        return gcd(a,b)