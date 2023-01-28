class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        result = [0 for x in temperatures]
        for i in range(len(temperatures)): 
            if len(stack) == 0:
                stack.append([temperatures[i], i])                  
            else:
                if stack[len(stack)- 1][0] < temperatures[i]:
                    while len(stack) != 0 and stack[len(stack)- 1][0] < temperatures[i]:
                        arr = stack.pop()
                        result[arr[1]] = i - arr[1]  
                    else:
                        stack.append([temperatures[i], i]) 
                else: stack.append([temperatures[i], i]) 
        return result
            
                        
                        
        