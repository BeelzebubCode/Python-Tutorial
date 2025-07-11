from collections import deque

def bfs_traverse(graph, start_node):
    visited = []
    queue = deque()
    seen = set()  # กันซ้ำใน queue

    queue.append(start_node)
    seen.add(start_node)

    while queue:
        node = queue.popleft()
        visited.append(node)

        children = sorted(graph[node])
        for child in children:
            if child not in seen:
                queue.append(child)
                seen.add(child)

    return visited

def display(arr):
    print("[",end="")
    for i in range(len(arr)):
        if i < len(arr)-1:
            print(f"\"{arr[i]}\"", end=", ")
        else:
            print(f"\"{arr[i]}\"", end="")
    print("]")

# --- อ่าน input ---
nodes = input().split()
graph = {node: [] for node in nodes}

for _ in range(len(nodes)):
    line = input().split()
    if line:  # เผื่อบางบรรทัดว่าง
        node = line[0]
        neighbors = line[1:]
        graph[node].extend(neighbors)  # เพิ่ม แทนการทับ


start = input().strip()

# --- BFS ---
result = bfs_traverse(graph, start)
display(result)
