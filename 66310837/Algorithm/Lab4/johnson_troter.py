def johnson_trotter_permutation(n, k):
    # กำหนดทิศทาง: -1 = ซ้าย, 1 = ขวา
    LEFT, RIGHT = -1, 1
    perm = [i for i in range(1, n + 1)]
    directions = [LEFT] * n
    result = [perm.copy()]
    
    def get_mobile():
        mobile_index = -1
        mobile_value = -1
        for i in range(n):
            next_index = i + directions[i]
            if 0 <= next_index < n and perm[i] > perm[next_index]:
                if perm[i] > mobile_value:
                    mobile_value = perm[i]
                    mobile_index = i
        return mobile_index
    
    while len(result) < k:
        mobile_index = get_mobile()
        if mobile_index == -1:  # ไม่มีตัวเคลื่อนที่ได้
            break
        
        # สลับตำแหน่ง
        next_index = mobile_index + directions[mobile_index]
        perm[mobile_index], perm[next_index] = perm[next_index], perm[mobile_index]
        directions[mobile_index], directions[next_index] = directions[next_index], directions[mobile_index]
        
        # เปลี่ยนทิศทางของตัวที่ใหญ่กว่าตัวที่สลับ
        swapped_value = perm[next_index]
        for i in range(n):
            if perm[i] > swapped_value:
                directions[i] *= -1
        
        result.append(perm.copy())
    
    return result[k - 1]

# ทดสอบ
n, k = map(int, input().split())
print(johnson_trotter_permutation(n, k))
