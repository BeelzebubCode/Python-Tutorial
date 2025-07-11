import math
import sys

def find_closest_pair(coords):
    min_dist = float('inf')
    n = len(coords)
    if n < 2:
        return 0.00  # หรือ -1 ถ้าไม่มีคู่ให้เปรียบเทียบ
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if dist < min_dist:
                min_dist = dist
    return min_dist

try:
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) % 2 != 0:
        # ถ้าเลขไม่ครบคู่ โยน error หรือจัดการเฉพาะคู่ที่สมบูรณ์
        print("0.00")
        sys.exit()
    coords = [(data[i], data[i+1]) for i in range(0, len(data), 2)]
    result = find_closest_pair(coords)
    print(f"{result:.2f}")
except:
    # กรณี input ผิด format หรือ error อื่นๆ
    print("0.00")
