n = list(map(int, input().split()))
is_sum = int(input())

index_sum = []
# -4 เพื่อกัน index เกิน
for i in range(len(n)-4):
    # ผลรวมของตำแหน่งปัจจุบัน i + กับ ตำแหน่งถัดไปอีก 4 ตำแหน่ง
    sum_of_five = sum(n[i:i+5]) # ถ้าเราไม่ -4 จะเกิด index เกินที่จุดนี้และ error
    if sum_of_five == is_sum: 
        # ถ้าผลรวม = ค่าที่เราต้องการ ให้เพิ่มไปใน list
        index_sum.append(i)

# ถ้าไม่ใช่ list ว่างจะแสดงข้อมูล index
if index_sum:
    for i in index_sum:
        print(i)
else:
    # ถ้าไม่เจอเลยจะปริ้น -1
    print(-1)
