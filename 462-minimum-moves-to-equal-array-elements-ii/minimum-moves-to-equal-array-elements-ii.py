class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        n = len(nums)

        nums.sort()

        median = nums[ n // 2]


        operations = 0

        for num in nums:
            operations+= abs(median - num)

        return operations


        