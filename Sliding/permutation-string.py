# This works slower compared to next function and use more space but its applicable to all kind of char
def permStringAll(s1: str, s2: str) -> bool:
    count1 = {}

    for ch in s1:
        count1[ch] = 1 + count1.get(ch, 0)
    
    need = len(count1)
    for i in range(len(s2)):
        count2, prev = {}, 0

        for j in range(i, len(s2)):
            count2[s2[j]] = 1 + count2.get(s2[j], 0)

            if count1.get(s2[j], 0) < count2[s2[j]]:
                break

            if count1.get(s2[j], 0) == count2[s2[j]]:
                prev += 1

            if prev == need:
                return True
    return False

# This solution is only accepted to lowercase characters 
def permString(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    count1 = [0] * 26
    count2 = [0] * 26

    for i in range(len(s1)):
        count1[ord(s1[i]) - ord('a')] += 1
    
    for i in range(len(s1)):
        count2[ord(s2[i]) - ord('a')] += 1
    
    if count1 == count2:
        return True

    for i in range(len(s1), len(s2)):
        count2[ord(s2[i]) - ord('a')] += 1
        count2[ord(s2[i - len(s1)]) - ord('a')] -= 1
    
        if count1 == count2:
            return True
        
    return False

s1 = "ABx"
s2 = "lexBAcabee"

print(permStringAll(s1, s2))
