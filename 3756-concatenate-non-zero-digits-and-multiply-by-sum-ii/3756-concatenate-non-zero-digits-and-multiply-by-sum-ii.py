from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        m = len(digits)

        if m == 0:
            return [0] * len(queries)

        # prefix digit sums
        prefixSum = [0] * (m + 1)
        for i in range(m):
            prefixSum[i + 1] = prefixSum[i] + digits[i]

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix concatenated values
        prefixVal = [0] * (m + 1)
        for i in range(m):
            prefixVal[i + 1] = (prefixVal[i] * 10 + digits[i]) % MOD

        ans = []

        for l, r in queries:

            L = bisect_left(pos, l)
            R = bisect_right(pos, r) - 1

            if L > R:
                ans.append(0)
                continue

            length = R - L + 1

            x = (
                prefixVal[R + 1]
                - prefixVal[L] * pow10[length]
            ) % MOD

            digitSum = prefixSum[R + 1] - prefixSum[L]

            ans.append((x * digitSum) % MOD)

        return ans