# Program to check whether a 
# given array represents a max-heap or not 

def isHeap(arr, i, n):

    if i > (n-1)//2:
        return True
    
    
    left = 2 * i + 1
    right = 2 * i + 2

    # check left child
    if arr[i] >= arr[left] and arr[i] >= arr[right] and isHeap(arr, left, n) and isHeap(arr, right, n):
        return True
    

    return False

   

    

# Driver Code
if __name__ == '__main__':
    arr = [90, 15, 10, 7, 12, 2, 70] 
    n = len(arr) - 1 

    print(isHeap(arr, 0, n))