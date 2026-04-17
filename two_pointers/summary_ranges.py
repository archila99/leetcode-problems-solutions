class Solution:
    def summaryRanges(self,nums):
        res = []
        l = 0
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i+1]:
                if l == i:
                    res.append(str(nums[l]))
                else:
                    res.append("{}->{}".format(nums[l], nums[i]))
                l = i + 1
        return res 

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,2,4,5,7]
    solution = sol.summaryRanges(nums)
    print(solution)