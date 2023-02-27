class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length


        