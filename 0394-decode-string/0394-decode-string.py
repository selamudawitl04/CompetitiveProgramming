class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        intValue = []
        for i in s:
            if len(stack) == 0: 
                if i.isdigit():
                    intValue.append(i)
                elif i == '[' and intValue:    
                    intValue = ''.join(intValue)
                    intValue = int(intValue)
                    stack.append(intValue)
                    stack.append(i)
                    intValue = []
                else:stack.append(i)
            else:
                if i == ']':
                    temp = []
                    while len(stack) != 0 and stack[len(stack) - 1] != '[':
                        temp.append(stack.pop())
                    else:
                        if len(stack) > 1: 
                            stack.pop()
                            num = int(stack.pop())
                            temp.reverse()
                            temp = temp * num
                            stack.extend(temp)
                else:
                    if i.isdigit():
                        intValue.append(i)
                    else:   
                        if intValue:
                            val = ''.join(intValue)
                            val = int(val)
                            stack.append(val)
                            intValue = []
                        stack.append(i)
        s = ''.join(stack)
        return s


        stack = []
        intValue = []
        for i in s:
            if len(stack) == 0: 
                if i.isdigit():
                    intValue.append(i)
                elif i == '[' and intValue:    
                    intValue = ''.join(intValue)
                    intValue = int(intValue)
                    stack.append(intValue)
                    stack.append(i)
                    intValue = []
                else:stack.append(i)
            else:
                if i == ']':
                    temp = []
                    while len(stack) != 0 and stack[len(stack) - 1] != '[':
                        temp.append(stack.pop())
                    else:
                        if len(stack) > 1: 
                            stack.pop()
                            num = int(stack.pop())
                            temp.reverse()
                            temp = temp * num
                            stack.extend(temp)
                else:
                    if i.isdigit():
                        intValue.append(i)
                    else:   
                        if intValue:
                            val = ''.join(intValue)
                            val = int(val)
                            stack.append(val)
                            intValue = []
                        stack.append(i)
        s = ''.join(stack)
        return s