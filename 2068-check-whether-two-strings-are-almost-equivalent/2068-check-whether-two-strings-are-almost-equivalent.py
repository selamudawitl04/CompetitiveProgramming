class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
    
        for i in word1:
            dict1[i]+= 1
        for j in word2:
            dict2[j]+= 1
        print(dict1,dict2)
        for s in dict1:
            if abs(dict1[s] - dict2[s]) > 3: return False
        for s in dict2:
            if abs(dict1[s] - dict2[s]) > 3: return False 
        return True
        
        