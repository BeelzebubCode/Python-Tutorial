
def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    r1 = l1 + w1
    b1 = t1 + h1
    r2 = l2 + w1
    b2 = t2 + h2

    if(r1 > l2 and r2 > l1 and b1 > t2 and b2 > t1):
        return True
    else:
        return False


l1, t1, w1, h1, l2, t2, w2, h2 = map(int, input().split(' '))
print(is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2))