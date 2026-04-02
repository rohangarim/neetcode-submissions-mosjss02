# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # calc total length of head
        # 2. iterate through linked list until reach left
        # 3. start at left and go to right (create new linked list)
        # 4. reverse that linked list
        # 5. new linkedlist that starts at head and tags onto new reversed linkedlist

        if (right - left) == 0:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(left -1 ):
            prev = prev.next
        reverse = prev.next
        curr = reverse
        prevv = None

        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prevv
            prevv = curr
            curr = temp
        prev.next = prevv
        reverse.next = curr

        return dummy.next
            