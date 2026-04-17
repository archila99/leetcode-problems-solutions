# naive approach

NUM_CHAR = 26

def isPermutation(txt, startIdx, pat):
    freq = [0] * NUM_CHAR

    for i in range(len(pat)):

        # increment one from frew if u see the that specific char in txt
        freq[ord(txt[startIdx + i]) - ord('a')] += 1

        # decrement one from freq if u see the specific char in pat
        freq[ord(pat[i]) - ord('a')] -= 1

    for i in range(NUM_CHAR):
        if freq[i] != 0:
            return False
    return True

def search1(txt, pat):
    n = len(txt)
    m = len(pat)

    for i in range(n - m + 1):
        if isPermutation(txt, i, pat):
            return True
        
    return False





# sliding window apperoach 
def check(freq):
    for i in range(NUM_CHAR):
        if freq[i] != 0:
            return False
    return True

def search(txt, pat):
    n = len(txt)
    m = len(pat)

    # constructing of first window 
    freq = [0] * NUM_CHAR
    for i in range(m):
        freq[ord(txt[i]) - ord('a')] += 1
        freq[ord(pat[i]) - ord('a')] -= 1

    # check for the first window
    if check(freq):
        return True
    
    for j in range(m, n):
        # Add the ith character into the window
        freq[ord(txt[j]) - ord('a')] += 1

        # Remove the (i - m)th character from the window
        freq[ord(txt[j - m]) - ord('a')] -= 1
        
         # Check for the current window
        if check(freq):
            return True
        
    return False
