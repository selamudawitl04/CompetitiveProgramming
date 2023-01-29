class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                temp = []
                while stack[len(stack) - 1] != '(':
                    temp.append(stack.pop())
                else: stack.pop()
                stack.extend(temp)
            else: stack.append(s[i])
        s = ''.join(stack)
        return s