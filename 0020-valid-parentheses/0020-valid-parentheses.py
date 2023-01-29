class Solution:
    def isValid(self, s: str) -> bool:
        mydict={
            "}":"{",
            "]":"[",
            ")":"("
        }
        test=[]
        for i in s:
            if i in mydict:
                if test and test[-1] == mydict[i]:
                    test.pop()
                else:
                    return False
            else:
                test.append(i)
                    
        return True if not test else False
    