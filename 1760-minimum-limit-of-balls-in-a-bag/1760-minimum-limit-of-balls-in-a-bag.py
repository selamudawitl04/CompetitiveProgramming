class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)
        minValue = left
        
        while left <= right:
            mid = (left + right)//2
            if self.valid(nums, maxOperations, mid):
                minValue = mid
                right = mid - 1
            else: left = mid + 1
                
        return minValue
     
    
    def valid(self, nums, h, k)->bool:
        if sum([math.ceil(x / k) - 1 for x in nums]) <= h: return True
        else: return False
        