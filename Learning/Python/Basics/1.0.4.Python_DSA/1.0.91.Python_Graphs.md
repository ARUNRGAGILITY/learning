# Graphs with LinkedList
Creating a graph data structure using a linked list involves representing the graph as an adjacency list. Each node in the linked list represents a vertex in the graph, and its connected nodes represent the vertices to which it is connected.

### Graph Implementation Using LinkedList

First, let's define the basic structure of the Graph and Node:

```python
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.adjacent = LinkedList()  # List of adjacent vertices

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = GraphNode(value)

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].adjacent.append(to_vertex)

    def display(self):
        for key, vertex in self.vertices.items():
            print(f"Vertex {key}: ", end='')
            vertex.adjacent.display()
```

### 10 Examples: From Basic to Advanced

#### 1. Creating a Simple Graph
```python
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_edge(1, 2)
g.display()  # Vertex 1: 2 -> None, Vertex 2: None
```

#### 2. Adding More Edges
```python
g.add_vertex(3)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.display()  # Vertex 1: 2 -> 3 -> None, Vertex 2: 3 -> None, Vertex 3: None
```

#### 3. Graph Traversal - Depth First Search (DFS)
```python
def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_vertex)
    print(start_vertex, end=' ')
    for adjacent_vertex in graph.vertices[start_vertex].adjacent:
        if adjacent_vertex not in visited:
            dfs(graph, adjacent_vertex, visited)

dfs(g, 1)  # Output: 1 2 3
```

#### 4. Graph Traversal - Breadth First Search (BFS)
```python
from collections import deque

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for adjacent in graph.vertices[vertex].adjacent:
                queue.append(adjacent)

bfs(g, 1)  # Output: 1 2 3
```

#### 5. Checking for a Path Between Two Vertices
```python
def has_path(graph, start_vertex, end_vertex):
    visited = set()
    return has_path_dfs(graph, start_vertex, end_vertex, visited)

def has_path_dfs(graph, current, end, visited):
    if current == end:
        return True
    visited.add(current)
    for adjacent in graph.vertices[current].adjacent:
        if adjacent not in visited:
            if has_path_dfs(graph, adjacent, end, visited):
                return True
    return False

print(has_path(g, 1, 3))  # Output: True
```

#### 6. Implementing Dijkstra's Algorithm (Shortest Path)
For this example, assume edges have weights. You'd need to modify the GraphNode and Graph classes to handle weights.

#### 7. Detecting Cycles in a Graph
Implement a cycle detection algorithm using DFS or BFS.

#### 8. Topological Sort
Implement topological sort for directed acyclic graphs (DAGs).

#### 9. Finding Connected Components
Use DFS or BFS to find all connected components in an undirected graph.

#### 10. Minimum Spanning Tree
Implement algorithms like Prim's or Kruskal's to find the minimum spanning tree of a graph.

These examples progress from simple graph creation and traversal to more advanced algorithms like shortest path finding and cycle detection. Each example builds on the previous ones, helping to deepen your understanding of graph theory and its practical applications in computer science.

Let's go through examples 6 to 10, implementing more advanced graph functionalities. These examples assume a more complex graph structure, possibly involving weights and directed edges. To keep things manageable, I'll provide simplified versions of these algorithms.

### 6. Implementing Dijkstra's Algorithm (Shortest Path)

First, modify the `GraphNode` class to handle weights. Then, implement Dijkstra's algorithm, which finds the shortest path from a start vertex to all other vertices in a weighted graph.

```python
import heapq

class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex][to_vertex] = weight

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0
        pq = [(0, start_vertex)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances
```

### 7. Detecting Cycles in a Graph

Detecting cycles in a directed graph can be done using DFS with recursion stack tracking.

```python
def is_cyclic(graph):
    visited = set()
    rec_stack = set()

    for vertex in graph.vertices:
        if vertex not in visited:
            if is_cyclic_util(graph, vertex, visited, rec_stack):
                return True
    return False

def is_cyclic_util(graph, current, visited, rec_stack):
    visited.add(current)
    rec_stack.add(current)

    for neighbor in graph.vertices[current]:
        if neighbor not in visited and is_cyclic_util(graph, neighbor, visited, rec_stack):
            return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(current)
    return False
```

### 8. Topological Sort

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering.

```python
def topological_sort(graph):
    visited = set()
    stack = []

    for vertex in graph.vertices:
        if vertex not in visited:
            topological_sort_util(graph, vertex, visited, stack)

    return stack[::-1]  # Return reversed stack

def topological_sort_util(graph, vertex, visited, stack):
    visited.add(vertex)
    for neighbor in graph.vertices[vertex]:
        if neighbor not in visited:
            topological_sort_util(graph, neighbor, visited, stack)
    stack.append(vertex)
```

### 9. Finding Connected Components

This function finds all connected components in an undirected graph.

```python
def find_connected_components(graph):
    visited = set()
    components = []

    for vertex in graph.vertices:
        if vertex not in visited:
            component = []
            dfs(graph, vertex, visited, component)
            components.append(component)

    return components

def dfs(graph, vertex, visited, component):
    visited.add(vertex)
    component.append(vertex)

    for neighbor in graph.vertices[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)
```

### 10. Minimum Spanning Tree - Prim's Algorithm

Prim's algorithm for finding a minimum spanning tree in a connected, undirected graph with weights.

```python
def prims_algorithm(graph, start_vertex):
    mst = set()
    visited = set([start_vertex])
    edges = [(weight, start_vertex, to) for to, weight in graph.vertices[start_vertex].items()]

    heapq.heapify(edges)

    while edges:
        weight, from_vertex, to_vertex = heapq.heappop(edges)
        if to_vertex not in visited:
            visited.add(to_vertex)
            mst.add((from_vertex, to_vertex, weight))

            for next_vertex, weight in graph.vertices[to_vertex].items():
                if next_vertex not in visited:
                    heapq.heappush(edges, (weight, to_vertex, next_vertex))

    return mst
```

These examples showcase intermediate to advanced graph algorithms. Remember, these implementations are simplified and may require adjustments for handling edge cases or specific requirements in real-world applications.

Let's explore practical examples for graph algorithms 1-5, illustrating their use in various scenarios.

### 1. Example: Creating a Simple Graph

**Scenario**: Build a network graph of a small office's computer system.

```python
office_graph = Graph()
for computer in ["PC1", "PC2", "Server", "Router"]:
    office_graph.add_vertex(computer)

office_graph.add_edge("PC1", "Router")
office_graph.add_edge("PC2", "Router")
office_graph.add_edge("Router", "Server")

office_graph.display()
```

### 2. Example: Adding More Edges

**Scenario**: Expand the office network by adding more connections.

```python
office_graph.add_vertex("PC3")
office_graph.add_edge("PC3", "Router")
office_graph.add_edge("Server", "PC3")

office_graph.display()
```

### 3. Example: Graph Traversal - Depth First Search (DFS)

**Scenario**: Traverse the office network to check connectivity from PC1.

```python
def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_vertex)
    print(start_vertex, end=' ')
    for adjacent_vertex in graph.vertices[start_vertex].adjacent:
        if adjacent_vertex not in visited:
            dfs(graph, adjacent_vertex, visited)

dfs(office_graph, "PC1")
```

### 4. Example: Graph Traversal - Breadth First Search (BFS)

**Scenario**: BFS traversal to check the network layers from the router.

```python
from collections import deque

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for adjacent in graph.vertices[vertex].adjacent:
                queue.append(adjacent)

bfs(office_graph, "Router")
```

### 5. Example: Checking for a Path Between Two Vertices

**Scenario**: Verify if there's a direct or indirect network path between two PCs.

```python
def has_path(graph, start_vertex, end_vertex):
    visited = set()
    return has_path_dfs(graph, start_vertex, end_vertex, visited)

def has_path_dfs(graph, current, end, visited):
    if current == end:
        return True
    visited.add(current)
    for adjacent in graph.vertices[current].adjacent:
        if adjacent not in visited:
            if has_path_dfs(graph, adjacent, end, visited):
                return True
    return False

print("Is there a path from PC1 to PC3?", has_path(office_graph, "PC1", "PC3"))
```

These examples demonstrate the use of basic graph algorithms in a small office network scenario. Such applications can be extended to larger networks, social graphs, transportation systems, and more, showcasing the versatility of graph algorithms in solving a wide range of problems.

Understood. Let's create practical examples using these advanced graph algorithms. We'll use hypothetical but realistic scenarios for each algorithm to illustrate how they can be applied.

### 6. Example: Shortest Path with Dijkstra's Algorithm

**Scenario**: Find the shortest path in a network of cities connected by roads with varying distances.

```python
# Create a graph of cities
city_graph = WeightedGraph()
for city in ["A", "B", "C", "D", "E"]:
    city_graph.add_vertex(city)

# Roads with distances
city_graph.add_edge("A", "B", 4)
city_graph.add_edge("A", "C", 1)
city_graph.add_edge("C", "B", 2)
city_graph.add_edge("B", "E", 3)
city_graph.add_edge("C", "D", 4)
city_graph.add_edge("D", "E", 1)

# Shortest path from A to E
shortest_paths = city_graph.dijkstra("A")
print("Shortest path from A to E:", shortest_paths["E"])
```

### 7. Example: Detecting Cycles in Course Prerequisites

**Scenario**: Check for cycles in course prerequisites to ensure there are no circular dependencies.

```python
# Create a graph of courses and their prerequisites
course_graph = Graph()
for course in ["Math", "Physics", "Chemistry", "Biology"]:
    course_graph.add_vertex(course)

course_graph.add_edge("Math", "Physics")
course_graph.add_edge("Physics", "Chemistry")
course_graph.add_edge("Chemistry", "Biology")
# Adding a cycle for demonstration
# course_graph.add_edge("Biology", "Math")

# Check for cycles
print("Does the course graph have a cycle?", is_cyclic(course_graph))
```

### 8. Example: Topological Sort in Task Scheduling

**Scenario**: Schedule tasks with dependencies in a manner that respects the order of dependencies.

```python
# Create a graph of tasks
task_graph = Graph()
for task in ["Write Code", "Test Code", "Deploy Code", "Design System"]:
    task_graph.add_vertex(task)

task_graph.add_edge("Design System", "Write Code")
task_graph.add_edge("Write Code", "Test Code")
task_graph.add_edge("Test Code", "Deploy Code")

# Topological sort to find a suitable task order
print("Task order:", topological_sort(task_graph))
```

### 9. Example: Finding Connected Components in a Social Network

**Scenario**: Identify groups of people who are connected (friends) within a social network.

```python
# Create a graph of people
social_graph = Graph()
for person in range(1, 6):  # Representing 5 people
    social_graph.add_vertex(person)

# Friendships
social_graph.add_edge(1, 2)
social_graph.add_edge(2, 3)
social_graph.add_edge(4, 5)

# Find connected components (friend groups)
print("Friend groups:", find_connected_components(social_graph))
```

### 10. Example: Minimum Spanning Tree in a Utility Network

**Scenario**: Plan the minimum cost of wiring for a new utility network connecting several buildings.

```python
# Create a graph of buildings and wiring costs
building_graph = WeightedGraph()
for building in ["A", "B", "C", "D"]:
    building_graph.add_vertex(building)

building_graph.add_edge("A", "B", 3)
building_graph.add_edge("A", "C", 1)
building_graph.add_edge("B", "C", 7)
building_graph.add_edge("B", "D", 5)
building_graph.add_edge("C", "D", 12)

# Find the minimum spanning tree (most cost-effective connections)
mst = prims_algorithm(building_graph, "A")
print("Minimum Spanning Tree:", mst)
```

Each of these examples demonstrates a practical use case for the corresponding algorithm, ranging from network planning and course scheduling to social network analysis and infrastructure development. They provide a glimpse into the diverse applications of graph theory in solving real-world problems.
