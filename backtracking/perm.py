# brute force 
class Solution:
    def brute_perm(self, nums):
        perms = [[]]
        for num in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
                    print(new_perms)
            perms = new_perms
        return perms

    def backtrack_perm(self, nums):
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res


    def backtrack(self, perm, nums, pick):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return 
        
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False


if __name__ == "__main__":
    nums = [1,2]
    sol = Solution()
    result = sol.backtrack_perm(nums)
    print(result)
    print(len(result))
