from collections import defaultdict
# solution with tuple 
def groupAnagrams(strs):
    seen = {}
    output = []
    for char in strs:
        sorted_char = tuple(sorted(char))
        if sorted_char in seen:
            output[seen[sorted_char]].append(char)

        else:
            seen[sorted_char] = len(output)
            output.append([char])
        
    return output


def groupAnagrams1(strs):
    groups = defaultdict(list)

    for char in strs:
        key = "".join(sorted(char))
        groups[key].append(char)
        
    return list(groups.values())
     

strs = ["tea","tan","ate","nat","bat", "eat"]

print(groupAnagrams1(strs))





