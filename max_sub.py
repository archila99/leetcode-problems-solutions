def minSubArrayLen(target, nums):
    n = len(nums)
    sum_window = 0
    left = 0
    min_len = float('inf')
    
    for right in range(n):
        sum_window += nums[right]

        while sum_window >= target:
            min_len = min(min_len, right - left +1)
            sum_window -= nums[left]
            left += 1
        
    return 0 if min_len == float('inf') else min_len