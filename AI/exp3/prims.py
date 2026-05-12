import heapq

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3),
        (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

def prim(graph, start):

    visited = set()

    min_heap = [(0, start, -1)]

    mst = []

    total_cost = 0

    while min_heap:

        cost, node, parent = \
            heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        if parent != -1:
            mst.append((parent,
                        node,
                        cost))

            total_cost += cost

        for neighbor, weight in graph[node]:

            if neighbor not in visited:
                heapq.heappush(
                    min_heap,
                    (weight,
                     neighbor,
                     node)
                )

    return mst, total_cost


mst, total = prim(graph, 0)

print("MST:", mst)
print("Total Cost:", total)