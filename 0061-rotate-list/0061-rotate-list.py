# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        tail = head
        numOfNodes = 1
        while tail.next:
            tail = tail.next
            numOfNodes += 1

        # Normalize k
        k = k % numOfNodes
        if k == 0:
            return head

        # Find new tail
        newTailPos = numOfNodes - k
        temp = head
        for _ in range(newTailPos - 1):
            temp = temp.next

        # Rotate
        tail.next = head
        head = temp.next
        temp.next = None

        return head
            

                