from typing import List

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        if target not in nums:
            return 0

        prefix = [0]
        cur = 0

        for x in nums:
            if x == target:
                cur += 1
            else:
                cur -= 1
            prefix.append(cur)

        vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = BIT(len(vals))

        ans = 0

        for p in prefix:
            idx = rank[p]
            ans += bit.query(idx - 1)
            bit.update(idx, 1)

        return ans