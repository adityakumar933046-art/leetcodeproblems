from typing import List
import math

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)

        def isPrime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False

            limit = int(math.sqrt(x))
            for i in range(3, limit + 1, 2):
                if x % i == 0:
                    return False
            return True

        ans = 0

        for i in range(n):
            if isPrime(nums[i][i]):
                ans = max(ans, nums[i][i])

            if isPrime(nums[i][n - 1 - i]):
                ans = max(ans, nums[i][n - 1 - i])

        return ans