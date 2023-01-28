class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dict1 = {}
        for i in nums1:
            dict1[i] = 0
        for val in nums2:
            if len(stack) == 0:
                stack.append(val)
            else:
                while len(stack) != 0 and stack[len(stack) - 1] < val :
                    if stack[len(stack) - 1] in dict1:
                        dict1[stack.pop()] = val
                    else: stack.pop()
                else: stack.append(val)
        print(stack)        
        for val in stack:
            print(val)
            if val in nums1:
                dict1[val] = -1
        result = []
        for i in dict1:
            result.append(dict1[i])
        return result