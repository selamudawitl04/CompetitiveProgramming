class MyQueue:

    def __init__(self):
        self.que = []

    def push(self, x: int) -> None:
        self.que.append(x)
        
    def pop(self) -> int:
        stack1 = []
        while len(self.que) != 0:
            stack1.append(self.que.pop())
        result = stack1.pop()
        while len(stack1) != 0:
            self.que.append(stack1.pop())
        return result

    def peek(self) -> int:
        stack1 = []
        while len(self.que) != 0:
            stack1.append(self.que.pop())
        result = stack1.pop()
        stack1.append(result)
        while len(stack1) != 0:
            self.que.append(stack1.pop())
        return result

    def empty(self) -> bool:
        return True if not self.que else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()