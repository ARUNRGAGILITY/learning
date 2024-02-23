# Search Algorithms

Search algorithms are typically categorized into two types: **linear search** and **binary search**. 
Beyond these, we will cover more advanced search algorithms often used in specific scenarios like searching in graphs or trees.

### 1. Linear Search

Linear search is the simplest search algorithm, where each element in a list is checked sequentially until the desired element is found or the list ends.

#### Example:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Target not found

# Example usage
arr = [5, 3, 8, 6, 1]
print(linear_search(arr, 8))  # Output: 2
```

### 2. Binary Search

Binary search is used on sorted arrays/lists. It divides the list into halves to check if the target is in the left or right half, repeatedly reducing the search area.

#### Example:

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid  # Target found
    return -1  # Target not found

# Example usage
sorted_arr = [1, 3, 5, 6, 8]
print(binary_search(sorted_arr, 5))  # Output: 2
```

### 3. Depth-First Search (DFS) in Graphs

DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It's often implemented using recursion or a stack.

#### Example:

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Example usage
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [1, 2]
}
print(dfs(graph, 0))  # Output: {0, 1, 2, 3}
```

### 4. Breadth-First Search (BFS) in Graphs

BFS is a graph traversal algorithm that starts at a selected node and explores all its neighbors at the present depth before moving on to nodes at the next depth level. It typically uses a queue.

#### Example:

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend([n for n in graph[vertex] if n not in visited])

    return visited

# Example usage
print(bfs(graph, 0))  # Output: {0, 1, 2, 3}
```

### 5. Jump Search

Jump search works on sorted arrays and is a block search algorithm. It creates a block and tries to find the element in that block. If the element is not there, it shifts the entire block. The optimal block size is √n.

#### Example:

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = math.sqrt(n)
    prev, next = 0, 0

    while next < n and arr[int(min(n, next) - 1)] < target:
        prev = next
        next += step

    for i in range(int(prev), int(min(n, next))):
        if arr[i] == target:
            return i  # Target found

    return -1  # Target not found

# Example usage
print(jump_search(sorted_arr, 6))  # Output: 3
```

### 6. Interpolation Search

Interpolation search is an improvement over binary search for instances, where the values in a sorted array are uniformly distributed. It positions the search at different locations based on the value of the target.

#### Example:

```python
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target: 
                return low
            return -1
        
        pos = low + int(((float(high - low) / (arr[high] - arr[low

])) * (target - arr[low])))

        if arr[pos] == target:
            return pos

        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Example usage
print(interpolation_search(sorted_arr, 6))  # Output: 3
```

### 7. Exponential Search

Exponential search combines the power of a Binary Search and the efficiency of jumping ahead by bounds. Initially, it jumps ahead in exponentially increasing steps, and once the range is narrowed, it uses binary search.

#### Example:

```python
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2
    return binary_search(arr[:min(index, len(arr))], target)

# Example usage
print(exponential_search(sorted_arr, 5))  # Output: 2
```

Each of these search algorithms has its own specific use case, advantages, and limitations. Linear and binary searches are fundamental and widely used, while DFS and BFS are essential for graph traversal. The other search methods are optimized for specific scenarios, such as sorted data or particular data distribution patterns.
