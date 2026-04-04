def merge(nums1, m, nums2, n):
    # here we trying to get last numbers of the sorted arrays because 
    # it will be the highest numbers if we compare them we will get the highest 
    # number therefore we can say that...
    i = m -1
    j = n-1
    k = m + n -1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else: 
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, m, nums2, n))
