
# Leetcode Problem 19: Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/



# Solution: Use two pointers, left and right. Move the right pointer n steps ahead, then move both pointers until the right pointer reaches the end of the list. The left pointer will be at the node before the one we want to remove. Update the next pointer of the left node to skip the nth node from the end.
# Time complexity: O(L) where L is the length of the linked list
# Space complexity: O(1) as we are using only constant space



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # left and right pointers 
        left = dummy 
        right = head 
        while n > 0 and right: 
            right = right.next 
            n-=1 

        while right : 
            left = left.next 
            right = right.next 

        
        left.next = left.next.next 

        return dummy.next 