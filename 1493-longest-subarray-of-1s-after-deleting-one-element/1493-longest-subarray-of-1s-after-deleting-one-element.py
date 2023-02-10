class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        windowStart = 0
        currentSum = 0
        maxSubArray = 0
        k = 1
        for i in range(len(nums)):
            currentSum+= 1
            if k == 0 and nums[i] == 0:
                maxSubArray = max(maxSubArray, currentSum - 1)
                while nums[windowStart] != 0:
                    print(nums[windowStart], currentSum)
                    currentSum-= 1
                    windowStart+= 1
                currentSum-= 1
                windowStart+= 1         
            elif k != 0 and nums[i] == 0:
                k = 0
        maxSubArray = max(maxSubArray, currentSum)
        return maxSubArray - 1

