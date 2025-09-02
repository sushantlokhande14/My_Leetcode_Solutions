# leetcode problem 138
# https://leetcode.com/problems/copy-list-with-random-pointer/  

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapp = {None : None}
        curr = head 
        while curr: 
            copy = Node(curr.val) # makes a new node , with no links 
            mapp[curr] = copy 
            curr = curr.next 

        
        curr = head 

        while curr:
            copy = mapp[curr]
            copy.next = mapp[curr.next] 
            copy.random = mapp[curr.random] 
            curr = curr.next

        
        return mapp[head]