from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Map to store frequency of characters in the current window
        count = defaultdict(int)

        n = len(s)
        result = 0
        left = 0  # Left pointer of sliding window

        for right in range(n):
            ch = s[right]

            # If the character appears less than 2 times, expand the window
            if count[ch] < 2:
                count[ch] += 1
                result = max(result, right - left + 1)

            else:
                # If the character already appeared twice,
                # shrink the window from the left until we remove one occurrence
                while s[left] != ch and left < right:
                    count[s[left]] -= 1
                    left += 1

                # Move past the previous occurrence of the same character
                left += 1

        return result