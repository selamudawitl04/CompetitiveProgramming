from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map1 = []
        result = []
        where = 0
        for val in s:
            j = len(map1) - 1
            exist = False
            while j >= 0:
                if val in map1[j]:
                    exist = True
                    length =  len(map1) - 1
                    while length > j:
                        for c in map1[length]:
                            map1[j][c]+= map1[length][c]
                        map1.pop()
                        length-= 1
                    map1[len(map1) - 1][val]+= 1
                    break
                j-= 1
            if exist == False:
                xc = defaultdict(int)
                xc[val] = 1
                map1.append(xc)
                del xc
        for b in map1:
            result.append(sum(b.values()))
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    