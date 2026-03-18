from collections import defaultdict
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # Important: handles subarrays starting at index 0

        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num

            # Check how many times (current_sum - goal) occurred before
            result += prefix_count[current_sum - goal]

            # Store current prefix sum
            prefix_count[current_sum] += 1

        return result