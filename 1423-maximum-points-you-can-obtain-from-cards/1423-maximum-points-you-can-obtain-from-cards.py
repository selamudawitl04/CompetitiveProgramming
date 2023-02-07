class Solution:
    def maxScore(self, cardPoints: list, k: int) -> int:
        minSum = float(inf)
        length = len(cardPoints)
        currentSum = 0
        windowStart = 0
        windowEnd = 0  
        k  =  len(cardPoints) - k
        if k == 0:
            return sum(cardPoints)
        for i in range(length):
            currentSum+= cardPoints[i]
            if i >= k - 1:
                tempMin = minSum
                minSum = min(minSum, currentSum)
                if tempMin > minSum:
                    windowStart = i + 1 - k
                    windowEnd = i
                currentSum-= cardPoints[i + 1 - k]
        for i in range(windowStart, windowEnd + 1):
            cardPoints[i] = 0
        print(cardPoints)
        maxSum = 0
        for val in cardPoints:
            maxSum+= val
            
        return maxSum