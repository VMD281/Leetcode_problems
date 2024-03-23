# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """  
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
      
        # Split the linked list into two halves
        second_half = slow.next
        slow.next = None
      
        # Reverse the second half of the linked list
        previous = None
        current = second_half
        while current:
            temp = current.next
            current.next = previous
            previous, current = current, temp
      
        # Merge the two halves, inserting nodes from the second half into the first
        first_half = head
        second_half = previous # This is now the head of the reversed second half.
        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next
          
            first_half.next = second_half
            second_half.next = temp1
          
            first_half, second_half = temp1, temp2
        