data = list(map(int, input().split()))
n = len(data) - 3
arr = data[:n]
x, y, z = data[n], data[n+1], data[n+2]

result = []

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
    
    # เก็บ index ของ x, y, z หลังจบ pass นี้
    result.append([arr.index(x), arr.index(y), arr.index(z)])

print(result)
