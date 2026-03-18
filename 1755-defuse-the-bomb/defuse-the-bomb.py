class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        n = len(code)

        result = [0] * n

        if k > 0:

            current_sum = 0

            for i in range( n + k):
                current_sum+= code[i % n]

                if i >= k :
                    current_sum-= code[i - k]
                    result[i - k] = current_sum

        elif k < 0:

            current_sum = 0

            for i in range(k, n):
                if i >= 0:
                    result[i] = current_sum
                    current_sum-= code[i - abs(k)]
                current_sum+= code[i]

        return result
        
            




        