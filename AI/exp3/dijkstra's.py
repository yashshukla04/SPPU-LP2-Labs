import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2),
          ('D', 5)],
    'C': [('A', 4), ('B', 2),
          ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def dijkstra(graph, start):

    dist = {
        node: float('inf')
        for node in graph
    }

    dist[start] = 0

    min_heap = [(0, start)]

    while min_heap:

        current_dist, current_node = \
            heapq.heappop(min_heap)

        for neighbor, weight in \
                graph[current_node]:

            distance = \
                current_dist + weight

            if distance < dist[neighbor]:

                dist[neighbor] = distance

                heapq.heappush(
                    min_heap,
                    (distance, neighbor)
                )

    return dist


distances = dijkstra(graph, 'A')

print("Shortest distances:",
      distances)