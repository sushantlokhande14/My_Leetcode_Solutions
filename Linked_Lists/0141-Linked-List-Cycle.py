# leetcode Problem 141: Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/


# solution 1: using hashset to store visited nodes
# time complexity : O(n) where n is the number of nodes in the linked list
# space complexity : O(n)   

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head 

        while curr: 
            if curr in seen: 
                return True 
            else: 
                seen.add(curr)
                curr = curr.next 

        return False 
    

# solution 2: using two pointers (Floyd's Tortoise and Hare algorithm)
# time complexity : O(n) where n is the number of nodes in the linked list
# space complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head 

        while fast and fast.next: 

            slow = slow.next 
            fast = fast.next.next


            if slow == fast: 
                return True 

        
        return False 