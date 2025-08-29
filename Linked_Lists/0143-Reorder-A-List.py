# Leetcode Problem 143. Reorder List    
# https://leetcode.com/problems/reorder-list/


# solution: find the middle of the linked list, reverse the second half, and merge the two halves
# time complexity : O(n) where n is the number of nodes in the linked list
# space complexity : O(1)

# I used three helper functions: splitList, reverseList, and mergeLists
# splitList uses the slow and fast pointer technique to find the middle of the linked list and split it into two halves
# reverseList reverses the second half of the linked list in place  
# mergeLists merges the two halves of the linked list by alternating nodes from each half


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next : 
            return 
        
        first, second = self.splitList(head)
        second = self.reverseList(second)   # can do inplace 
        self.mergeLists(first, second)
        
    
    def splitList(self,head):
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        second = slow.next 
        slow.next = None # cuts the list 
        return head, second 
    
    def reverseList(self, head):
        prev = None 
        curr = head 

        while curr: 
            tmp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = tmp 

        return prev 

    def mergeLists(self, l1, l2):

        while l1 and l2: 

            n1 = l1.next 
            n2 = l2.next 

            l1.next = l2 
            l2.next = n1 

            l1 = n1 
            l2 = n2 
