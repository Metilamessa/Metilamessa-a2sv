# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sorted_head = head
        unsorted = head.next
        sorted_head.next = None

        while unsorted:
            curr = unsorted
            unsorted = unsorted.next

            if curr.val < sorted_head.val:
                curr.next = sorted_head
                sorted_head = curr
            else:
                prev = sorted_head
                while prev.next and prev.next.val < curr.val:
                    prev = prev.next
                curr.next = prev.next
                prev.next = curr

        return sorted_head
