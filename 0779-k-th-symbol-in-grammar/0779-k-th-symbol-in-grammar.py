class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1 or n == 1: return 0
        length = int(math.pow(2, n -1))
        mid = length//2
        print(mid)
        if mid >= k:
            return self.kthGrammar(n - 1, k)
        else: return self.kthGrammar(n - 1, k - mid)^1
        

