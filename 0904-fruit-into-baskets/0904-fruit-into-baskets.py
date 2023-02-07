class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        windowStart = 0
        currentSum= 0
        maxNumber = 0
        Map = {}
        for val in fruits:
            currentSum+= 1
            if val in Map:
                Map[val]+= 1
            else: Map[val] = 1
            if len(Map) > 2:
                while len(Map) > 2:
                    if Map[fruits[windowStart]] > 1:
                        Map[fruits[windowStart]]-= 1
                    else: 
                        del Map[fruits[windowStart]]
                    currentSum-= 1
                    windowStart+=1
            else: maxNumber = max(maxNumber, currentSum)
        return maxNumber
            
        