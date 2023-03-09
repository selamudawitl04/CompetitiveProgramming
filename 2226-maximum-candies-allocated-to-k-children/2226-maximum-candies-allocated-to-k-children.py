class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        right = max(candies)
        maxValue = 0 
        while left <= right:
            mid = (left + right)//2
            if mid == 0: 
                left = 1
                continue
            if self.valid(candies, mid, k):
                maxValue = mid
                left = mid + 1
            else: right = mid - 1                
        return maxValue
    
    def valid(self, nums, mid, k)->bool:
        if sum([math.floor(x / mid) for x in nums]) >= k: return True
        else: return False
        