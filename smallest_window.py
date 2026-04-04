def smallest(S):
    res = 999999

    # to check 0, 1, 2
    zero = 0
    one = 0
    two = 0

    zero_index = 0
    one_index = 0
    two_index = 0

    for i in range(len(S)):
        if S[i] == 0:
            zero = 1
            zero_index = i

        elif S[i] == 1:
            one = 1
            one_index = i

        elif S[i] == 2:
            two = 1
            two_index = i

        if zero and one and two:
            res = min(res, max(zero_index, one_index, two_index) -  min(zero_index, one_index, two_index))
        
    if res == 999999:
        return -1
    
    return res + 1

S = [0, 1, 1, 2, 2, 0]

# a solutoin w sliding window 

def smallestSub(S):
    n = len(S)
    i = 0
    j = 0
    k = 0
    cnt = 0
    min_len = float("inf")

    # frequency array where to check the occurence of the 0 1 2 initially set 0
    freq = [0] * 3

    while k < n:
        freq[int[S[k]]] += 1
        if freq[int[S[k]]] == 1:
            cnt += 1
        
        if cnt == 3:
            while freq[int[S[i]]] > 1:
                freq[int(S[i])] -= 1
                i += 1
            min_len = min(min_len, k - i + 1)
            if min_len == 3:
                return 3 
            freq[int(S[i])] -= 1
            i += 1
            cnt -= 1
        k += 1

    return -1 if min_len == float("inf") else min_len


# Now lets try to find the smallest substring 
# containing all characters from a given set, like 'a','b','c','d'.

def smallestSubChar():
    S = "abccdd"
    chars = {
        'a', 
        'b',
        'c',
        'd'
    }

    freq = {ch: 0 for ch in chars}
    i = 0
    cnt = 0
    min_len = float("inf")

    for k in range(len(S)):
        if S[k] in freq:
            freq[S[k]] += 1
            if freq[S[k]] == 1:
                cnt += 1
        
            while cnt == len(chars):
                min_len = min(min_len, k - i + 1)
                if S[i] in freq:
                    freq[S[i]] -= 1
                    if freq[S[i]] == 0:
                        cnt -= 1
                
                i += 1
        
    
    return -1 if min_len == float("inf") else min_len

print(smallestSubChar())



