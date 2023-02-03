class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i != 0:
                nums[i] = nums[i] + nums[i - 1]
        for j in range(len(nums)):
            if j == 0:
                if nums[len(nums) - 1] - nums[j] == 0:
                    return 0
            else:
                 if nums[len(nums) - 1] - nums[j] == nums[j - 1]:
                        return j
        return -1
                