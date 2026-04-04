class Solution(object):
    def moveZeroes(self, nums):
        last_num = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_num] = nums[i]
                last_num += 1
        
        for i in range(last_num, len(nums)):
            nums[i] = 0
    

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    solution = sol.moveZeroes(nums)
    print(nums)