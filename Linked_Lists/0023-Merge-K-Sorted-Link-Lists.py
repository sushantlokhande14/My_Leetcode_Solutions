# leetcode 23 Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# brute force solution
# time complexity O(N log N) where N is total number of nodes in all the lists
# space complexity O(N) for storing all the nodes in a list

# here we are using python's inbuilt sort function which uses Timsort algorithm
# Timsort has a time complexity of O(N log N) in the average and worst
# case, and O(N) in the best case (when the array is already sorted).


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for head in lists: 
            while head: 
                nodes.append(head.val)
                head = head.next 
        
        nodes.sort()

        res = ListNode(0)
        curr = res 
        for node in nodes: 
            curr.next = ListNode(node)
            curr = curr.next 

        return res.next 
 