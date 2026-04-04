def prefixCount(words, pref):
    """
    :type words: List[str]
    :type pref: str
    :rtype: int
    """
    result = 0
    for char in words:
        count = 0
        if len(pref) <= len(char):
            for i in range(len(pref)):
                if pref[i] == char[i]:
                    count += 1
                else:
                    break
                
        if count == len(pref):
            result += 1
    
    return result

def prefixCount2(words, pref):
    return sum(char.startswith(pref) for char in words)

words = ["lewsmb","lewrydnve","lewqqm","lewec","liwn","lewb","lewedb"]
pref = "lew"

a = prefixCount2(words, pref)
print(a)