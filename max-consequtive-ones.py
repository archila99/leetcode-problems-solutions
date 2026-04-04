def maxConsequtive(arr, k):
    n = len(arr)
    if n < k:
        return -1
    

arr = [0, 1, 1, 0, 1]
k = 2

print(maxConsequtive(arr, k))