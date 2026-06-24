from heapq import heappush, heappop
from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:

        g = defaultdict(list)

        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, 2 * w))

        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            d, u = heappop(pq)

            if d > dist[u]:
                continue

            for v, w in g[u]:
                nd = d + w

                if nd < dist[v]:
                    dist[v] = nd
                    heappush(pq, (nd, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]