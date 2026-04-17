def remove(nums, val):
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] != val:
            i += 1
            j += 1
        else:
            nums.remove(val)
        
        
    
    return i

nums = [3,2,2,3]
val = 3

print(remove(nums, val))