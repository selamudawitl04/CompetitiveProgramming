class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minValue = right
        
        while left <= right:
            mid = (left + right)//2
            if self.valid(piles, h, mid):
                minValue = mid
                right = mid - 1
            else: left = mid + 1
                
        return minValue
    
    
    def valid(self, nums, h, k)->bool:
        if sum([math.ceil(x / k) for x in nums]) <= h: return True
        else: return False