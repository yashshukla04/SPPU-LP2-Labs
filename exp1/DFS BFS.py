# BFS traversal for undirected graph

graph = {
    'A': ['B', 'C'],
    'B': ['A' ,'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

Visited = []
Queue = []

def bfs(node):
    Visited.append(node)
    Queue.append(node)

    while Queue:
        m = Queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in Visited:
                Visited.append(neighbour)
                Queue.append(neighbour)

    
    
print("BFS Traversal:")
bfs('A')


# DFS traversal for undirected graph(Recursive)
Visited = set()

def dfs(V):
    Visited.add(V)
    print(V, end=" ")

    for i in graph[V]:
        if i not in Visited:
            dfs(i)
print("\nDFS Traversal:")
dfs('A')
