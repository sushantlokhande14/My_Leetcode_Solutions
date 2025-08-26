# Leetcode 0206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/    

# Iterative Approach    - Time Complexity: O(n) - where n is the number of nodes in the linked list
# Space Complexity: O(1) - no extra space used


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        prev = None 

        while curr: 
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        
        return prev
    

# Recursive Approach - Time Complexity: O(n) - where n is the number of nodes in the linked list
# Space Complexity: O(n) - the recursion stack can go up to n   

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or only one node, return head
        if not head or not head.next:
            return head  

        # Reverse the rest of the list
        newHead = self.reverseList(head.next)

        # Flip the pointer
        head.next.next = head
        head.next = None

        return newHead 