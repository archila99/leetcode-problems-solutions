class Solution:
    def combinationSum(self, nums, target):
        self.res = []
        self.backtracking(nums, target, 0, [], 0)
        return self.res
    def backtracking(self, nums, target, i, cur, total):
            if total == target:
                self.res.append(cur.copy())
                return
            if total > target or i >= len(nums):
                return 
            cur.append(nums[i])
            self.backtracking(nums, target, i, cur, total + nums[i])
            cur.pop()
            self.backtracking(nums, target, i + 1, cur, total)

if __name__ == "__main__":
    nums = [2,3,6,7]
    target = 7
    sol = Solution()
    result = sol.combinationSum(nums, target)
    print(result)