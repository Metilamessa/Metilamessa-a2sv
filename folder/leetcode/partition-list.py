# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:


        dummy_before = ListNode(0)
        dummy_after = ListNode(0)
        before_curr = dummy_before
        after_curr = dummy_after
        
        while head:
            if head.val < x:
                before_curr.next = head
                before_curr = before_curr.next
            else:
                after_curr.next = head
                after_curr = after_curr.next
            head = head.next
        
        after_curr.next = None
        before_curr.next = dummy_after.next
        
        return dummy_before.next
