class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = {}
        prefixSumCount[0] = 1
        countSubArray = 0
        sum = 0
        for i in range(len(nums)):
            sum+= nums[i]
            if sum - k in prefixSumCount:
                countSubArray+= prefixSumCount[sum - k]
            if sum in prefixSumCount:
                prefixSumCount[sum]+= 1
            else: prefixSumCount[sum] =  1
        return countSubArray