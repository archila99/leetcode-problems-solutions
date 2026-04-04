def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:

        mid = low + (high - low)//2

        #Check if x is present at mid
        if arr[mid] == x:
            return mid
        
        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

        # If we reach here, then the element was not present
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40, 48]
    x = 48

    result = binarySearch(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")


def binarySearch(arr, low, high, x):

    # Check base case 
    if high >= low:
        mid = low + (high - low)//2

        # if elemetn is present at the middle itslef
        if arr[mid] == x:
            return mid
        
        # if element is smaller than mid, then it can
        # only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # I f element is smaller than mid, then it 
        # can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    # if element is not present in the array
    else:
        return -1