# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listVal = []
        while head:
            listVal.append(head.val)
            head = head.next
        i=0
        j = len(listVal) - 1
        while j > i and listVal[i] == listVal[j]:
            i+=1
            j-=1
        return i >= j
