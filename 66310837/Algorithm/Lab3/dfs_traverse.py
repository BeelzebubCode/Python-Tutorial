def dfs_traverse(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # เพิ่มลูกเข้า stack ตามลำดับที่ให้ (ต้องย้อนลำดับ เพราะ stack LIFO)
            children = graph[node]
            for child in reversed(children):
                if child not in visited:
                    stack.append(child)
    return visited


def display(arr):
    print("[", end="")
    for i in range(len(arr)):
        if i < len(arr) - 1:
            print(f"\"{arr[i]}\"", end=", ")
        else:
            print(f"\"{arr[i]}\"", end="")
    print("]")


# อ่าน input
nodes = input().split()
graph = {node: [] for node in nodes}

for _ in range(len(nodes)):
    line = input().split()
    node = line[0]
    neighbors = line[1:] if len(line) > 1 else []
    graph[node] = neighbors

start = input().strip()

result = dfs_traverse(graph, start)
display(result)
