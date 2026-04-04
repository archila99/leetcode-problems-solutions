# this coed is for string solution 

def isPalindrome(x):
    s = str(x) # converting a number to a string
    i = 0
    j = len(s) - 1
 
  # looping until i < j
    while(i < j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

x = 12221



# mathematical solution 

def isPalindrome2(x):
    if x < 0:
        return False
    
    original = x
    reverse = 0

    while(original > 0):
        last_digit = original % 10.  # getting the last number from or.
        reverse = reverse * 10 + last_digit 
        original = original // 10
    
    return reverse == x
    

print(isPalindrome2(x))