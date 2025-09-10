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
 

 # Optimal solution using divide and conquer approach
# time complexity O(N log k) where N is total number of nodes in all the lists and k is number of lists
# space complexity O(1) for storing all the nodes in a list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)== 0: 
            return None 


        while len(lists)> 1: 
            mergedLists = []
            for i in range(0 , len(lists), 2): 
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)< len(lists) else None
                res = self.mergeLists(l1, l2)
                mergedLists.append(res)
            lists = mergedLists
        
        return lists[0]


    
    #helper func
    def mergeLists(self, l1, l2): 
        dummy = ListNode(0)
        tail = dummy 
        while l1 and l2: 
            if l1.val > l2.val: 
                tail.next = l2
                l2 = l2.next 
            else: 
                tail.next = l1 
                l1 = l1.next 
            
            tail = tail.next 

        if l1 : 
            tail.next = l1 
            
        if l2 : 
            tail.next = l2 
            
        return dummy.next 