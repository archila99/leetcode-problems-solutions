# To heapify a subtree rooted with node i
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # if right vhild is larger than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)



def heapSort(arr):
    n = len(arr)

    # Build heap (rearrange vector)
    for i in range(n//2 - 1, -1 , -1):
        heapify(arr, n, i)
    
    # One by one extract an element from heap
    for i in range(n-1, 0, -1):
        # One by one extract an element from heap
        arr[0], arr[i] = arr[i], arr[0]

        # call max heapify on the reduced heap
        heapify(arr, i, 0)



if __name__ == "__main__":
    arr = [4, 1, 2, 5, 10, 11, 3]

    heapSort(arr)

    for i in range(len(arr)):
        print(arr[i], end=" ")