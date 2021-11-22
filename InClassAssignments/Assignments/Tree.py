from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = 12

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, root):
        visited = [False] * (self.nodes+1)
        print(len(visited))
        q = []
        q.append(root)
        visited[root] = True

        while len(q) != 0:
            root = q.pop(0)
            print(root, end= ' ')

            for i in self.graph[root]:
                if visited[i]== False:
                    q.append(i)
                    visited[i] = True

    def dfs(self, visited, node):
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbour in self.graph[node]:
                self.dfs(visited, neighbour)
        
    def printGraph(self):
        print(self.graph)

    
g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)

g.printGraph()
g.BFS(1)
visited = set()
g.dfs(visited, 1)

#Time and Space Complexity O(v+e)    