
def CheckSubset(a, b):

    # Check which list is smaller 
    if len(a) < len(b):
        smaller, larger = a, b
    else:
        smaller, larger = b, a

    #Convert the smaller list to set for faster lookup
    my_set = set(smaller)

    # Check if any element of the larger list exists in the small set
    for n in larger:
        if n in my_set:
            return True
    return False


b = [1, 2, 3]
a = [1]

print(CheckSubset(a, b))




