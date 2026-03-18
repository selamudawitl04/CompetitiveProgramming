from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted = [0] * n  # Final decrypted result

        # Case k > 0 → sum of next k elements
        if k > 0:
            window_sum = 0

            # Loop over circular array with extra k elements for wrap-around
            for i in range(n + k):
                window_sum += code[i % n]  # Add current element to window

                if i >= k:
                    # Remove element leaving the window
                    window_sum -= code[i - k]
                    # Assign sum to the correct index in result
                    decrypted[i - k] = window_sum

        # Case k < 0 → sum of previous |k| elements
        elif k < 0:
            window_sum = 0
            # Use absolute value of k
            k = abs(k)

            for i in range(-k, n):
                if i >= 0:
                    decrypted[i] = window_sum
                    window_sum -= code[i - k]  # Remove element leaving the window
                window_sum += code[i]  # Add current element to window

        # Case k == 0 → all zeros (already initialized)
        return decrypted