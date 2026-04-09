class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        n = len(nums)
        max_value = nums[-1]
        count = 0

        for i in range(n - 2, -1, -1):

            if nums[i] <= max_value:
                max_value = nums[i]
                continue

            parts = (nums[i] + max_value - 1) // max_value
            count += parts - 1
            max_value = nums[i] // parts

        return count