# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        tail = head 
        length =1
        while tail.next:
            tail = tail.next
            length +=1
        k = k % length
        if k == 0:
            return head
        tail.next = head
        steps = length - k
        new_tails = head
        for _ in range(steps -1):
            new_tails = new_tails.next
        new_head = new_tails.next
        new_tails.next = None
        return new_head
           
