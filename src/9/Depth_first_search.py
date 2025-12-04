class Graph:
    graph = {}
    DFS_VISIT = []
    index = 0

    def __init__(self):
        self.add_vertex("A")
        self.add_vertex("B")
        self.add_vertex("C")
        self.add_vertex("D")
        self.add_vertex("E")
        self.add_vertex("F")

        self.add_edge("A", "B")
        self.add_edge("A", "C")
        self.add_edge("A", "D")

        self.add_edge("B", "C")

        self.add_edge("C", "D")

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph.get(vertex1).append(vertex2)

        self.graph.get(vertex2).append(vertex1)

    def DFS_step(self, vertex, visited):
        if vertex not in visited:
            visited.append(vertex)

            links = self.graph.get(vertex)
            for link in links:
                self.DFS_step(link, visited)

    def DFS(self, startVertex):
        if self.graph.get(startVertex) is None:
            return []

        visited = []
        self.DFS_step(vertex=startVertex, visited=visited)

        self.DFS_VISIT = visited
        return visited

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.DFS_VISIT):
            vertex = self.DFS_VISIT[self.index]
            self.index += 1

            return vertex

        self.index = 0
        raise StopIteration

    def __str__(self):
        return str(self.graph)


if __name__ == '__main__':
    graph = Graph()
    print("Graph: ", graph)

    print("\nDFS route: ", graph.DFS(startVertex="A"))

    print("\niterable")
    for i in graph:
        print(i, end=" ")
