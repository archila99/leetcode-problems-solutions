# this solution is o(n2) complexity
def twoSum(nums, target):
    
    for i in range(len(nums)):
        x = target - nums[i] # here we getting complemented number 

        # here we looking if we have that complemented 
        # element in the array after the current selected
        if x in nums[i+1:]:
            j = nums[i+1:].index(x) + (i + 1) # find the original index of the second element
            return [i, j]
    
    return None

# this solution is O(n) complexity
def twoSum2(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return None
        


nums = [1,2,3]
target = 4
print(twoSum2(nums, target))