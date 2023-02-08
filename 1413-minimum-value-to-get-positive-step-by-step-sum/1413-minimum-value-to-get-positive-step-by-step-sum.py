class Solution:
    def minStartValue(self, nums: List[int]) -> int:  
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
            print(nums)
        if min(nums) < 1:
                return -1 * min(nums) + 1
        else: return 1
            
        