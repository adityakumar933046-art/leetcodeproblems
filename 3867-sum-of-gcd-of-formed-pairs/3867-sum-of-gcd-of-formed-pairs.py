from typing import List
from math import gcd

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefix = []
        mx = 0

        # Construct prefixGcd
        for x in nums:
            mx = max(mx, x)
            prefix.append(gcd(x, mx))

        # Sort
        prefix.sort()

        # Pair smallest with largest
        ans = 0
        i, j = 0, len(prefix) - 1

        while i < j:
            ans += gcd(prefix[i], prefix[j])
            i += 1
            j -= 1

        return ans