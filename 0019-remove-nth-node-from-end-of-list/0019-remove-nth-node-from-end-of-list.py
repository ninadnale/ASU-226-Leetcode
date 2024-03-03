# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head.next and n>=1):
            return None
        
        dummy = ListNode(0, head)
        
        fwd_ptr = rem_ptr = dummy

        for i in range(n+1):
            fwd_ptr = fwd_ptr.next
        
        while(fwd_ptr):
            fwd_ptr = fwd_ptr.next
            rem_ptr = rem_ptr.next
        
        if(rem_ptr==dummy):
            return rem_ptr.next.next
        
        rem_ptr.next = rem_ptr.next.next if(rem_ptr.next) else None

        return head
        