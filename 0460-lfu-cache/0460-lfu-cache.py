class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1

class LinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_at_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        node.prev.next = nxt
        node.next.prev = prev

    def remove_tail(self): 
        if self.is_empty():
            return None
        node = self.tail.prev
        self.remove(node)
        return node
    
    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.freq_to_nodes = defaultdict(LinkedList)
        self.min_freq = 0
        self.size = 0

    def update_freq(self, node):
        freq = node.freq
        self.freq_to_nodes[freq].remove(node)
        if freq == self.min_freq and self.freq_to_nodes[freq].is_empty():
            self.min_freq += 1
        node.freq += 1
        self.freq_to_nodes[node.freq].insert_at_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.update_freq(node)
            return
        if self.size == self.capacity:
            lfu_node = self.freq_to_nodes[self.min_freq].remove_tail()
            del self.key_to_node[lfu_node.key]
            self.size -= 1
        
        new_node = Node(key, value)
        self.freq_to_nodes[1].insert_at_head(new_node)
        self.key_to_node[key] = new_node
        self.min_freq = 1
        self.size += 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)