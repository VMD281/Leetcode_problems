# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)   #introduce a dummy node
        
        #introduce a left pointer
        left = dummy
        
        #introduce a right pointer
        right = head
        
        #add a loop for the right pointer
        while n>0 and right:
            right = right.next
            n -= 1
        
        #keep incrementing both pointers till we reach the end of the linkedlist i.e            right = NULL
        while right:
            left = left.next
            right = right.next
        
        #deleting the node
        left.next = left.next.next
        return dummy.next