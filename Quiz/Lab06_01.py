
def triangle(n):
    star = '*'
    starEnd = '* '
    space = '.'
    result = ''
    for i in range(1,n+1):
        for j in range(1, (2*i-1)+1):
            if i == n:
                result+=starEnd*n
                return result
            if(j == 1 or j == 2*i-1):
                result+=star
            else:
                result+=space
        result+='\n'

    return result

num = int(input())
print(triangle(num))