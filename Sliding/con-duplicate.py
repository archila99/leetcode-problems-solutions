
#return true if nums[i] == nums[j] or false
# it should comply to this abs(i-j) <= k

# Brute Force Solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums)) ):
                if nums[i] == nums[j]:
                        return True
            
        return False
    
nums = [1, 2, 4, 0, 1]
k = 5
    
obj = Solution()
result = obj.containsNearbyDuplicate(nums, k)

# Hash Map Solution
class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i
        
        return False
    

obj1 = Solution2()
result1 = obj1.containsNearbyDuplicate(nums, k)

print(result1)