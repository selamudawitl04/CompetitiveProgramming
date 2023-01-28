class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        poppedPointer = 0
        pushedPointer = 0
        stack = []
        while pushedPointer <= len(pushed):
            if len(stack) != 0:
                if stack[len(stack) - 1] == popped[poppedPointer]:
                    stack.pop()
                    poppedPointer+= 1

                else:
                    if pushedPointer == len(pushed): break
                    stack.append(pushed[pushedPointer])
                    pushedPointer+= 1
            else: 
                if pushedPointer == len(pushed): break
                stack.append(pushed[pushedPointer])
                pushedPointer+= 1
        return len(stack) == 0 
        