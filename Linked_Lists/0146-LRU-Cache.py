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

