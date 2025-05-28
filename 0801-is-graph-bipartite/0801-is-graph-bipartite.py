class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                q = deque([i])
                color[i] = 0
                while q:
                    node = q.popleft()
                    for nbr in graph[node]:
                        if color[node] == color[nbr]:
                            return False
                        elif color[nbr] == -1:
                            color[nbr] = 1 - color[node]
                            q.append(nbr)
        return True