# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        sentinel = ListNode(None)
        sentinel.next = head
        
        left = right = sentinel # left is the end node of the left part list, vice versa.

        while left == right and right.next != None:
            if right.next.val < x:
                left = right = right.next
            else:
                right = right.next
        
        while right.next != None:
            if right.next.val >= x:
                right = right.next
                continue
            else:
                # move to correct location
                misplaced_node = right.next
                right.next = right.next.next
                
                misplaced_node.next = left.next
                left.next = misplaced_node
                left = left.next

        return sentinel.next
        
