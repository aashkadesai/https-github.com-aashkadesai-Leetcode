class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            max_time = max(max_time, time)

            for nbr, t in graph[node]:
                if nbr not in visited:
                    heapq.heappush(min_heap, (t + time, nbr))
        return max_time if len(visited) == n else -1