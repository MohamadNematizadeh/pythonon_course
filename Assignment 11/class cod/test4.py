def amir(n):
    if n == 0 :
        return 1
    else:
        return n * amir(n-1)

print(amir(30))            