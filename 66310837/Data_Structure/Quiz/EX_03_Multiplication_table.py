try:
    n = int(input())

    for i in range(1, 13):
        print("%d x %d = %d" % (n, i, n*i))
except ValueError:
    print("Too much input!") 
  