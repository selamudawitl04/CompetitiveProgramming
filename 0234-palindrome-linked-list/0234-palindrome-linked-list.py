class Solution:
    def mid(self,head):
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def reverse(self,head):
        prev,curr=None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:return 1
        midHead=self.mid(head).next
        midHead=self.reverse(midHead)
        while midHead:
            if head.val!=midHead.val:return 0
            head=head.next
            midHead=midHead.next
        return 1