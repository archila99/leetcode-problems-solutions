def maxSum(arr, k):
    # length of an array
    n = len(arr)

    # n must be greater than k
    if n < k:
        print("Invalid")
        return -1
    
    # Compute sum of first window of size k
    window_sum = sum(arr[:k])

    # first sum available
    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum

arr = [1,1,1,4,1,1]
k = 2

print(maxSum(arr, k))
