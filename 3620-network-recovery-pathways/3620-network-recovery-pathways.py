from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indeg = [0] * n

        mx = 0
        for u, v, w in edges:
            graph[u].append((v, w))
            indeg[v] += 1
            mx = max(mx, w)

        # Topological sort
        q = deque()
        topo = []
        deg = indeg[:]

        for i in range(n):
            if deg[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)

        INF = 10**30

        def check(mid):
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < mid:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    dp[v] = min(dp[v], dp[u] + w)

            return dp[n - 1] <= k

        lo, hi = 0, mx
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans