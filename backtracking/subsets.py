# find all the possible subsets of the given array 
# solving it with backtracking
def subsets(nums):
    result = []

    def backtrack(index, path):
        # Base case
        if index == len(nums):
            result.append(path[:])
            return

        # Decision 1: Iclude nums[index]
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()


        # # Decision 2: skip nums[index]
        backtrack(index + 1, path)


    backtrack(0, [])
    return result

# solving it with stack and tuples
def subsets2(nums):
    result = []
    stack = []
    stack.append((0, []))

    while stack:
        index, subset = stack.pop()

        if index == len(nums):
            result.append(subset)
            continue
        
        # OPTION 1: skip nums[index]
        stack.append((index + 1, subset))

        # OPTION 2: include nums[index]
        new_subset = subset + [nums[index]]
        stack.append((index + 1, new_subset))
    
    return result


nums = [1,2]
print(subsets2(nums))

# output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]