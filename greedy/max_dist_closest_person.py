class Solution:
    def maxDistToClosest(self, seats):
        result = 0
        prev = None

        for i in range(len(seats)):
            if seats[i] == 1:
                if prev == None:
                    result = i
                else:
                    result = max(result, (i - prev)//2)
                prev = i

        result = max(result, len(seats) - 1 - prev)
        return result 

if __name__ == "__main__":
    sol = Solution()
    seats = [0,0,0,0,1,0,1]
    solution = sol.maxDistToClosest(seats)
    print(solution)