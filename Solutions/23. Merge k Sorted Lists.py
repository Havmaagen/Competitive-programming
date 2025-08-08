# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        answer = ListNode()
        current_node = answer
        
        heap = [(node.val, node) for node in lists if node]
        heapify(heap)
        while heap:
            _, node = heappop(heap)
            current_node.next = node
            current_node = current_node.next
            
            if node.next:
                node = node.next
                heappush(heap, (node.val, node))
        
        answer = answer.next
        
        return answer