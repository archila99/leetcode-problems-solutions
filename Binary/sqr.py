
# solution with recursion 
def sqr(low, high, x):
    if low <= high:
        mid = low + (high - low) // 2

        if mid == x // mid:          # check exact square root
            return mid
        elif mid  < x // mid:         # mid too small, search right
            return sqr(mid + 1, high, x)
        else:                       # mid too big, search left
            return sqr(low, mid - 1, x)
    
    return -1  # not found

print(sqr(0, 49, 49))  


# solution with binary search

def sqr2(x):
    low = 0
    high = x
    while low <= high:
        mid = low + (high - low) // 2

        if mid == x // mid:
            return mid
        
        elif mid > x // mid:
            high = mid - 1

        else:
            low = mid + 1
    else:
        return -1

print(sqr2(10))
    

