# This solution outputs the remained element of the array of stones where 
# randomly array of intigers stones is given and select stones[i] = y max and 
# x stones[ith] second heaviest and if x == y remove that from array
# if y > x push back remainder y - x to an array and continue untill 
# yoiu checked all the elements and return if theere is one last left
# or 0 if nothing left
import heapq

def lastStoneWeight(arr):
    max_heap = []
    
    for i in range(len(arr)):
        heapq.heappush(max_heap, -1 * arr[i])

    print(max_heap)
    
    while len(max_heap) > 1:
        first_pop = heapq.heappop(max_heap)
        second_pop = heapq.heappop(max_heap)

        if second_pop != first_pop:
            heapq.heappush(max_heap, first_pop - second_pop)

    
    if len(max_heap) != 0:
        return  -max_heap[0]

    return 0
    

    
stones = [2,7,4,1,8,1]

a = lastStoneWeight(stones)
print(a)