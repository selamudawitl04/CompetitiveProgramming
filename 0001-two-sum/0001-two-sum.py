class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(len(nums)):
            Map[nums[i]] = i
        print(Map)
            
        for val in nums:
            if target-val in Map:
                if target - val == val:
                    if nums.count(val) > 1:
                        return [nums.index(val), Map[val]]
                else:
                    return [Map[val], Map[target - val]]
                
        
        return [0,1]


