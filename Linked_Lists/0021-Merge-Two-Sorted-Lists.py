# Leetcode Problem 21: Merge Two Sorted Lists       
# https://leetcode.com/problems/merge-two-sorted-lists/


# time complexity : O(n + m) where n and m are the lengths of the two lists  
# space complexity : O(1)   

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 

        while list1 and list2: 
            if list1.val < list2.val: 
                tail.next = list1 
                list1 = list1.next

            else : 
                tail.next = list2
                list2 = list2.next 

            tail = tail.next  
        

        if list1: 
            tail.next = list1 
        
        if list2: 
            tail.next = list2 

        
        return dummy.next 