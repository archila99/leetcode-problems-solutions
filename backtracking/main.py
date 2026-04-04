def rec(x):
    if x == 0:
        return
    
    print(0)
    rec(x-1)
    print(1)

    rec(x-1)

rec(2)