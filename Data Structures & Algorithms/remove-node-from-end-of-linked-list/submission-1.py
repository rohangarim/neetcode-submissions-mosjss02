# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        test = head
        while test:
            count += 1
            test = test.next
        size = count - n

        if size == 0:
            return head.next
        # [1,2,3,4,5], n = 3
        # [0,1,2,3,4], count = 5 - 3 = 2
        curr = head
        for i in range(count -1):
            if (i+1) == size:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head