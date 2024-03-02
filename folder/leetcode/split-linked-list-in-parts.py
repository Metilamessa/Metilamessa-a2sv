# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        list_length = 0
        current = head
        while current:
            list_length += 1
            current = current.next

        part_size = list_length // k
        remainder = list_length % k
        current = head
        result = []
        for i in range(k):
            part_head = current  
            part_length = part_size + (1 if i < remainder else 0)

            for _ in range(part_length - 1):
                current = current.next

            if current:
                next_node = current.next
                current.next = None
                current = next_node

            result.append(part_head)  

        return result