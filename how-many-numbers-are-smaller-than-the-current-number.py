class Solution:
    def numberOfSmaller(self,nums, target):
        nums.sort()
        return nums.index(target)
    def smallerNumbersThanCurrent(self, nums):
        return [ self.numberOfSmaller(nums[:], x) for x in nums]
