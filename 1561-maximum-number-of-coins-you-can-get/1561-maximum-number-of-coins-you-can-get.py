class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxNumber = 0
        head = 0
        tail = len(piles) - 1
        while head < tail:
            maxNumber+= piles[tail - 1]
            tail-= 2
            head+= 1
        return maxNumber
        