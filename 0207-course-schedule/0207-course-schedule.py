class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0

        while q:
            course = q.popleft()
            visited += 1
            for nbr in graph[course]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        return visited == numCourses
            