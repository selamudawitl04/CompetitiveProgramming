class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while stack and stack[-1] > n and k > 0:
                k -= 1
                stack.pop()
            stack.append(n)
        if k > 0:
            stack = stack[:-k]
        result = "".join(stack)
        
        return str(int(result)) if len(stack) else "0"