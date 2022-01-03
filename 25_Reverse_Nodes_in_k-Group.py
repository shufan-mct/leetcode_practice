class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:               
        def reverseK(node, k):
            # reversed the first K node of the list
            # return new head and tail of it
            prev = None
            curr = node
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return (prev, node)
        
        def forwardK(node, k):
            curr = node
            for i in range(k):
                if curr:
                    curr = curr.next
                else:
                    return (False, None)
            return (True, curr)
        
        dummy = ListNode(0)
        prevTail = dummy
        
        curr = head
        kth = forwardK(curr, k)
        while kth[0]:
            rcHead, rcTail = reverseK(curr, k)
            prevTail.next = rcHead
            prevTail = rcTail
            curr = kth[1]
            kth = forwardK(curr, k)

            
        if curr is not None:
            prevTail.next = curr
            
        return dummy.next