from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        startWindow = 0
        result = []
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in range(len(p)):
            dict1[p[i]]+= 1
        print(dict1)
        for i in range(len(s)):
            if s[i] not in p and i < len(s) - 1:
                startWindow =  i + 1
                dict2.clear()
            else:
                dict2[s[i]]+= 1
                if i - startWindow == len(p)-1:
                    if len(dict1.items() & dict2.items()) == len(dict1):
                        result.append(startWindow)
                        dict2[s[startWindow]]-= 1
                        startWindow+= 1
                    else:
                        dict2[s[startWindow]]-= 1
                        startWindow+= 1
                 
        return result

