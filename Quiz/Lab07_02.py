# ไม่สำเร็จ
def square_frame(n, sep=' '):
    num = 1
    for i in range(1,n+1):
        for j in range(1,n*2):
            if i == 1 or i == n:
                if j%2 != 0:
                    print(num,end='')
                    num+=1
                else:
                    print(sep,end='')
            else:
                if j == 1 or j == n*2-1:
                    print(num,end='')
                else:
                    print(sep,end='')

        print()
    

square_frame(3)