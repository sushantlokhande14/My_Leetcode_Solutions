# leetcode 25 : Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# solution using stack
# time complexity O(N) where N is number of nodes in the linked list
# space complexity O(k) where k is the size of the stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1 : 
            return head 

        dummy = ListNode()
        dummy.next = head 
        prev = dummy 
        curr = head 

        while True: 

            stack = []
            node = curr
            for i in range(k): 
                if not node : 
                    prev.next = curr 
                    return dummy.next 
                
                stack.append(node)
                node = node.next 

            prev.next = stack.pop()
            tail = prev.next 
            while stack: 
                tail.next = stack.pop()
                tail = tail.next 

            #reconnect 
            tail.next = node 
            prev = tail 
            curr = node 
  
  # Optimal solution without using extra space
# time complexity O(N) where N is number of nodes in the linked list
# space complexity O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr