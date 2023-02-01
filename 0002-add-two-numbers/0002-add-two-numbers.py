# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # to store the result
        result = ListNode(0)
        def insertEnd(val)->None:
            itrator = result
            while itrator.next:
                itrator = itrator.next
            itrator.next = ListNode(val)    
        rm = 0
        while l1 or l2:
            x = l1.val if l1 else 0 
            y = l2.val if l2 else 0 
            if  x + y + rm - 10 >= 0:
                insertEnd((x + y + rm)%10)
                rm = 1
            else:
                insertEnd(x + y + rm)
                rm = 0
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if rm == 1: 
            insertEnd(1)
          
        return result.next
            