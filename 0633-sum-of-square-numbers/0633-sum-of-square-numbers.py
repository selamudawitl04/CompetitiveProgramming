class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        tail = math.ceil(math.sqrt(c))
        head = 0
        while head <= tail:
            if head * head + tail * tail == c:
                return True
            elif head * head + tail * tail < c:
                head+= 1
            else: tail-= 1
        return False