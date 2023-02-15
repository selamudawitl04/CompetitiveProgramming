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
        