class Solution:
    def intToRoman(self, num: int) -> str:
        def toRoman(numDigit, num)->str:
            if num == 0 : return ''
            print(numDigit, num)
            hashMap = {
                1 : 'I', 4 : 'IV', 5 : 'V', 9 : 'IX', 10 : 'X', 40 : 'XL',
                50 : 'L',
                90 : 'XC',
                100 : 'C',
                400 : 'CD',
                500 : 'D',
                900 : 'CM',
                1000 : 'M'
            }
            
            if num / numDigit == 4 or num / numDigit == 9:
                return hashMap[num][::-1]
            elif num / numDigit < 5:
                return (hashMap[numDigit] * (num // numDigit))[::-1]
            elif num / numDigit > 5:
                dig = int(num / numDigit)
                print(dig)
                return  (hashMap[numDigit * 5] + hashMap[numDigit] * (dig - 5))[::-1]
            else: return hashMap[numDigit * 5]
        
        result = ''
        string = str(num)
        for i in range(1, len(str(num))+1):
            nums = int(string[-i]) * int(math.pow(10,i - 1))
            result+= toRoman(int(math.pow(10,i - 1)), nums )
        return result[:: -1]
            
            
            
        