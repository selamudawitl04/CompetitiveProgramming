
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        # Store frequency of remainders of 60
        m = defaultdict(int)

        result = 0
        
        for t in time :

            remainder = t % 60
            result+= m[(60 - remainder) % 60]

            m[remainder]+= 1


        return result