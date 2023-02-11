class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(len(nums)):
            if target - nums[i] in Map:
                return [i, Map[target - nums[i]]]
            Map[nums[i]] = i
        return None
            
        
