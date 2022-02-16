public class Solution {
    public ListNode SwapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;
        ListNode future;
        
        while (curr != null && curr.next != null){
            future = curr.next.next;
            prev.next = curr.next;
            curr.next.next = curr;
            prev = curr;
            curr = future;
        }
        prev.next = curr;
        
        return dummy.next;
    }
}