class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        result = ''
        minString = str('a')* 300
        for j in strs:
            if len(j) < len(minString):
                minString = j
        for i in range(len(minString)):
            for st in strs:
                if st[i] != minString[i]: return result
            result+= minString[i]
        return result
    
