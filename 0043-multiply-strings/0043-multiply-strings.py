class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = '0' * (len(num1) - len(num2)) + num2
        elif len(num2) > len(num1):
            num1 = '0' * (len(num2) - len(num1)) + num1
        remender = 0
        result = ''
        for i in range(len(num1) - 1, -1, -1) :
            Sum = int(num1[i]) + int(num2[i]) + remender
            if Sum >= 10:
                result = str(Sum % 10) + result
                remender = 1
            else:
                result = str(Sum) + result
                remender = 0
        if remender != 0: return '1' + result  
        return result
    def multiply(self, num1: str, num2: str) -> str:
        if num1.count('0') == len(num1) or num2.count('0') == len(num2): return '0'
        result = '0'
        for i in range(len(num1) - 1, -1, -1):
            temp = ''
            rem = 0
            for j in range(len(num2) - 1, -1, -1):
                tempMul = int(num1[i]) * int(num2[j]) + rem 
                if tempMul >= 10:
                    temp = str(tempMul % 10) + temp
                    rem = int(str(tempMul)[ :len(str(tempMul)) - 1])
                else: 
                    temp = str(tempMul) + temp
                    rem = 0
            if rem != 0: temp = str(rem) + temp
            temp = temp + '0' * (len(num1) - i - 1)
            result = self.addStrings(result, temp) 
        return result
                    

                    
                    
                

        
        
        