from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        order = sorted(range(n), key=lambda i: nums[i])

        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i

        nxt = list(range(n))

        j = 0
        for i in range(n):
            while j + 1 < n and nums[order[j + 1]] - nums[order[i]] <= maxDiff:
                j += 1
            nxt[i] = j

        LOG = 20
        up = [[0] * n for _ in range(LOG)]
        up[0] = nxt[:]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:

            if u == v:
                ans.append(0)
                continue

            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            if nxt[l] == l:
                ans.append(-1)
                continue

            steps = 0
            cur = l

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    steps += 1 << k

            if nxt[cur] >= r:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans