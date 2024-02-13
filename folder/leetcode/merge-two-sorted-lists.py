# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_list1 = list1
        curr_list2 = list2

        result = ListNode()
        head = result
        while curr_list1 or curr_list2:
            if curr_list1 and curr_list2:
                if curr_list1.val <= curr_list2.val:
                    head.next = ListNode(curr_list1.val)
                    head = head.next
                    curr_list1 = curr_list1.next
                else:
                    head.next = ListNode(curr_list2.val)
                    head = head.next
                    curr_list2 = curr_list2.next
            elif curr_list1:
                head.next = curr_list1
                break
            else:
                head.next = curr_list2
                break


        

        return result.next
         

        