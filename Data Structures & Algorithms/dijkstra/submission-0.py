class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {i: [] for i in range(n)}
        for u, v, w in edges:
            graph[u].append((v, w))

        distances = [float('inf')] * n
        done = [False] * n
        pq = []

        heapq.heappush(pq, (0, src))
        distances[src] = 0

        while pq:
            # ExtractMin
            current_dist, current = heapq.heappop(pq)

            if done[current]:
                continue

            done[current] = True

            for neighbor, weight in graph[current]:
                # Edge relaxation
                if not done[neighbor]:
                    new_dist = current_dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        # Format result
        result = {}
        for i in range(n):
            if distances[i] == float('inf'):
                result[i] = -1
            else:
                result[i] = distances[i]
        
        return result