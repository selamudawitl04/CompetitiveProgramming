class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        head = 0
        tail = len(nums) - 1
        maxValue = -inf
        while head < tail :
            maxValue = max(maxValue, nums[head] + nums[tail])
            head+= 1
            tail-= 1
            
        return maxValue




        
        