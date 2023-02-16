from decimal import Decimal
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            if len(sentence[i]) > 1 and sentence[i][0] == '$' and sentence[i][1: ].isdigit():
                num = float(sentence[i][1:])
                num-= num * (discount/100)
                num = Decimal(num)
                num = round(num, 2)
                sentence[i] = '$' + str(num)
        sentence = ' '.join(sentence)
        return sentence
        