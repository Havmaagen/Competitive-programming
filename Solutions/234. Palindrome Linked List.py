# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        node1, node2 = head, prev
        while node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        
        return True