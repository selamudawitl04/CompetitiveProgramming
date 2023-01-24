from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0  or len(s) == 1:
            return len(s)
        dict = defaultdict(int)
        startWindow = 0
        longestMax = 0
        currentMax = 0
        for i in range(len(s)):
            currentMax+= 1
            if dict[s[i]] != 0 :
                longestMax = max(longestMax, currentMax -1)
                while(s[startWindow] != s[i]):
                    dict[s[startWindow]]-= 1
                    startWindow+= 1
                    currentMax-= 1
                startWindow+= 1
                currentMax-= 1
            else:
                dict[s[i]]+= 1
        longestMax = max(longestMax, currentMax)    
        return longestMax
