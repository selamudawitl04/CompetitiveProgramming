class Solution:
    def findKthBit(self, n: int, k: int) -> str:  
        if n == 1 or k == 1:
           return '0'
        mid = (int(math.pow(2, n)))//2 
        print(mid)
        if k < mid:
            return self.findKthBit(n - 1, k)
        elif mid == k:
            return '1'
        else:
            return str(int(self.findKthBit(n - 1, 2 * mid - k))^1)
            

        