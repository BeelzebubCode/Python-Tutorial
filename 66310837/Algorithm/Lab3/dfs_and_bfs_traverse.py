from collections import deque

def dfs_exit(graph, start, exit_node):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node == exit_node:
            return True
        if node not in visited:
            visited.add(node)
            # เพิ่มลูก node ตามลำดับที่ให้ (ไม่ต้องเรียง)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return False

def bfs_shortest_path(graph, start, exit_node):
    visited = set()
    queue = deque()
    queue.append((start, 0))  # (node, distance)
    visited.add(start)

    while queue:
        node, dist = queue.popleft()
        if node == exit_node:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1


# --- อ่าน input ---
n = int(input())
nodes = input().split()

graph = {node: [] for node in nodes}
for _ in range(n):
    line = input().split()
    node = line[0]
    neighbors = line[1:] if len(line) > 1 else []
    graph[node] = neighbors

start = input().strip()
exit_node = input().strip()

# --- เรียกใช้ฟังก์ชัน ---
print("dfs_exit:", dfs_exit(graph, start, exit_node))
print("bfs_shortest_path:", bfs_shortest_path(graph, start, exit_node))
