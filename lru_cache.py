class Node:
    def __init__(self, key: int, val: int): # external node class
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node

        # left = LRU, right = MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right # link the 2 inital nodes together for doubly linked list
        self.right.prev = self.left

    # remove node from list
    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # insert node at MRU (right side)
    def _insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.cache: # not found
            return -1
        node = self.cache[key] # get node 
        self._remove(node) # remove from linked list 
        self._insert(node) # add to right end of linked list (most recently used)
        return node.val # return val for the key

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # remove curr node in mapping 
            self._remove(self.cache[key])

        self.cache[key] = Node(key, value) # make new node 
        self._insert(self.cache[key]) # add to rigth end of linked list 

        if len(self.cache) > self.cap:
            # remove LRU from list and dict
            lru = self.left.next # remove least used node (left most node in linked list )
            self._remove(lru) # remove from list 
            del self.cache[lru.key] # remove key from mapping