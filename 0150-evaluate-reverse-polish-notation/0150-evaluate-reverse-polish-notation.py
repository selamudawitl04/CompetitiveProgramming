
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for token in tokens:
            if len(token) == 1 and token == '+' or token == '-' or token == '*' or token == '/':
                y = result.pop()
                x = result.pop()
                if token == '+': result.append(x + y)
                elif token == '-': result.append(x - y)
                elif token == '*': result.append(x * y)
                else: 
                    result.append(math.trunc(x / y))
            else: 
                result.append(int(token))
        return int(result[0])





