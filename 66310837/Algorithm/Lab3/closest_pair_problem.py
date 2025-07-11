import math
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 10  # กำหนดความแม่นให้พอ

def find_closest_pair(points):
    if len(points) < 2:
        return "0.00"

    min_dist = float('inf')
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            dist = math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
            min_dist = min(min_dist, dist)

    # ใช้ Decimal ปัดแบบ ROUND_HALF_UP (ปัดขึ้นเมื่อ .005)
    decimal_dist = Decimal(str(min_dist)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{decimal_dist:.2f}"

# อ่าน input
raw_input = sys.stdin.read().strip()

if not raw_input:
    print("0.00")
else:
    raw = raw_input.split()
    if len(raw) % 2 != 0:
        print("0.00")
    else:
        try:
            nums = list(map(int, raw))
            points = [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]
            print(find_closest_pair(points))
        except ValueError:
            print("0.00")

