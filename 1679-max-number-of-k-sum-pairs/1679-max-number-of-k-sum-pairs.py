class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        head = 0
        tail = len(nums) - 1
        numberOfOperation = 0
        while head < tail:
            if nums[head] + nums[tail] == k:
                numberOfOperation+= 1
                head+= 1
                tail-= 1
            elif nums[head] + nums[tail] < k:
                head+= 1
            else: 
                tail-= 1
        return numberOfOperation


