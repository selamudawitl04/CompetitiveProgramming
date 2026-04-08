class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        count  = 0 
        n = len(nums)

        for i in range(1, n):
            if nums[i] <= nums[i - 1] :
                count+= nums[i - 1] - nums[i]  + 1
                nums[i] = nums[i - 1] + 1
    
        return count


#  1 1 2 2 3 7

c  = 1