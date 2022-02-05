public class Solution {
    public ListNode MergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode, int> heap = new PriorityQueue<ListNode, int>();
        
        foreach (ListNode head in lists){
            if (head != null){
                heap.Enqueue(head, head.val);
            }            
        }
        
        ListNode dummyHead = new ListNode();
        ListNode curr = dummyHead;
        
        while (heap.TryDequeue(out ListNode head, out int val)){
            ListNode newHead = head.next;
            if (newHead != null){
                heap.Enqueue(newHead, newHead.val);
            }
            head.next = null;
            curr.next = head;
            curr = curr.next;                        
        }
        
        return dummyHead.next;
    }
}