class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b): b = str('0')* (len(a) - len(b)) + b
        else: a = str('0')* (len(b) - len(a)) + a
        a = a[:: -1]
        b = b[:: -1]
        rm = 0
        sumString = ''
        for i in range(len(a)):
            if int(a[i]) + int(b[i]) + rm > 2: 
                sumString+= str('1')
                rm = 1
            elif int(a[i]) + int(b[i]) + rm == 2: 
                sumString+= str('0')
                rm = 1
            else: 
                sumString+= str(int(a[i]) + int(b[i]) + rm)
                rm = 0
        if rm == 1: sumString+= '1'    
        return sumString[:: -1]
       
        