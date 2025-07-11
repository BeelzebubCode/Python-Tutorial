import sys

def find_convex_hull(points):
    # ลบจุดซ้ำ และเรียงตาม x, แล้ว y
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    # cross product เพื่อเช็คทิศการโค้ง
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # สร้าง lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # สร้าง upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # รวม hull (ลบจุดซ้ำตรงหัวท้าย)
    return lower[:-1] + upper[:-1]


input = sys.stdin.readline

raw = list(map(int, input().strip().split()))
points = [(raw[i], raw[i+1]) for i in range(0, len(raw), 2)]
print(find_convex_hull(points))
