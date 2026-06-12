class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = math.ceil(math.log2(n + 1))

        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        stack = [1]
        visited = [False] * (n + 1)
        visited[1] = True

        while stack:
            node = stack.pop()

            for nei in g[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    parent[0][nei] = node
                    stack.append(nei)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(a, b):

            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]

            for k in range(LOG):
                if diff & (1 << k):
                    a = parent[k][a]

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if parent[k][a] != parent[k][b]:
                    a = parent[k][a]
                    b = parent[k][b]

            return parent[0][a]

        ans = []

        for u, v in queries:

            w = lca(u, v)

            L = depth[u] + depth[v] - 2 * depth[w]

            if L == 0:
                ans.append(0)
            else:
                ans.append(pow(2, L - 1, MOD))

        return ans