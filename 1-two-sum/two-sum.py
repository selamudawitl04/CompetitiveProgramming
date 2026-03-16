class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = dict()
        for i in range(len(nums)) :
            required = target - nums[i]
            if required in nMap :
                return [nMap[required], i]
            
            nMap[nums[i]] = i
        
        
           
        