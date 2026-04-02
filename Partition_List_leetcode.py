# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        less_dummy = ListNode(0)
        greate_dummy = ListNode(0)

        less = less_dummy
        greater = greate_dummy
        while head:
         if head.val <x:
            less.next = head
            less=less.next
         else:
            greater.next = head
            greater = greater.next
         head = head.next
        less.next =  greate_dummy.next 
        greater.next = None
        return less_dummy.next
