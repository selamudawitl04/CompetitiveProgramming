class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        for i in range(length - 2):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j]!= nums[k]:
                        count+=1
        return count

        