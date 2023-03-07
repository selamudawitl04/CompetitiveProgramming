class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(1,len(nums) - 1):
            if nums[i] + diff in nums and nums[i] - diff in nums:
                count+= 1
        return count