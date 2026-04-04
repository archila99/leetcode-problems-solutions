class Solution:
    def validAnagram(self, s, t):
        if len(s) != len(t):
            return False

        seen = {}
        for ch in s:
            if ch not in seen:
                seen[ch] = 1
            else:
                seen[ch] += 1
        
        for ch in t:
            if ch not in seen:
                return False
            seen[ch] -= 1
        
        for ch in seen:
            if seen[ch] != 0:
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    solution = sol.validAnagram(s,t)
    print(solution)