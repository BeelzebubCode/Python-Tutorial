def gray_code_kth(n, k):
    def generate_gray(n):
        if n == 1:
            return ['0', '1']
        prev = generate_gray(n - 1)
        return ['0' + code for code in prev] + ['1' + code for code in reversed(prev)]

    codes = generate_gray(n)
    return codes[k]

# ทดสอบ
n, k = map(int, input().split())
print(f"'{gray_code_kth(n, k)}'")
