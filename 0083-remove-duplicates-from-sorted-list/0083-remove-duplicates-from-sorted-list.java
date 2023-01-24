/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return null;
        ListNode travel = head;
        while(travel.next != null){
            if(travel.val == travel.next.val){
                travel.next = travel.next.next;
            }else
                travel = travel.next;
        }
        return head;
    }
}