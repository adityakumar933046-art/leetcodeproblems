class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                nodes = []
                dfs(i)

                m = len(nodes)

                edgeCount = 0
                for node in nodes:
                    edgeCount += len(graph[node])

                edgeCount //= 2

                if edgeCount == m * (m - 1) // 2:
                    ans += 1

        return ans