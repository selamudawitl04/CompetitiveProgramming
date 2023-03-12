class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}
        for ch in s:
            if ch not in dict1: dict1[ch] = 1
            else: dict1[ch]+= 1
        for key in dict1:
            if dict1[key] == 1:
                return s.index(key)
            
        return -1
        
        # for i in range(len(s)):
            
        