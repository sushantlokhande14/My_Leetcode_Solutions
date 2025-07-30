
class ListNode: 
    def __innit__(self, val, next_node=None):
        self.val = val 
        self.next = next_node 
 


class LinkedList:
    
    def __init__(self):
        #Dummy
        self.head = ListNode(-1)
        self.tail = self.head 

    
    def get(self, index: int) -> int:

        curr = self.head.head
        i = 0 

        while curr : 
            if i == index: 
                return curr.value 
            curr= curr.next 
            i += 1 

        return -1 # index error 
    
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next 
        self.head.next = new_node
        # list was empty before inserting 
        if not new_node.next: 
            self.tail = new_node 

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next 


    def remove(self, index: int) -> bool:
        

    def getValues(self) -> List[int]:
        
