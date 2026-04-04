# solution with remove slower
def removeDuplicates(nums):
    i = 0
    while(i < len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i])
        else:
            i += 1
    return nums


# faster solution

def removeDuplicates2(nums):
    if not nums:
        return 0
    
    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:  # found unique number
            i += 1
            nums[i] = nums[j]


    return i + 1

print(removeDuplicates2([1,1,1,2]))