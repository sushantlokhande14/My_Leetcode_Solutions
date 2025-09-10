# Leetcode 146 LRU Cache
# https://leetcode.com/problems/lru-cache/

# brute force  
# time complexity O(N) where N is total number of nodes in all the lists
# space complexity O(N) for storing all the nodes in a list

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = []

    def get(self, key: int) -> int:
        
        for i ,(k,v) in enumerate(self.cache): 
            if k == key :
                self.cache.pop(i)
                self.cache.insert(0, (k,v))
                return v 
        return -1 

    def put(self, key: int, value: int) -> None:
        for i, (k,v) in enumerate(self.cache):
            if k == key : 
                self.cache.pop(i)
                self.cache.insert(0, (key, value))
                return 
            
        if len(self.cache) == self.capacity : 
            self.cache.pop()
            
        self.cache.insert(0, (key,value))
        

# Optimal solution for LRU Cache
# time complexity O(1) for both get and put operations
# space complexity O(N) for storing all the nodes in a list

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]