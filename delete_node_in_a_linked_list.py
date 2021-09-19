"""
Ques. Delete node in a linked list 
T.C. = O(1)
S.C. = O(1)
Link - https://leetcode.com/problems/delete-node-in-a-linked-list/
"""
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next