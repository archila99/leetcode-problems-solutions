def move(nums):
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            k = nums[i]
            nums[i] = nums[j]
            nums[j] = k
            i += 1
            
    return nums
nums = [0, 0, 1, 0]
print(move(nums))