# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None

# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.cache = {}
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         node.prev.next = nxt
#         node.next.prev = prev

#     def add_to_front(self, node):
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self.cache:
#             return -1
#         node = self.cache[key]
#         self.remove(node)
#         self.add_to_front(node)
#         return node.val

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if key in self.cache:
#             self.remove(self.cache[key])
#         node = Node(key, value)
#         self.cache[key] = node
#         self.add_to_front(node)
        
#         if len(self.cache) > self.capacity:
#             lru = self.tail.prev
#             self.remove(lru)
#             del self.cache[lru.key]


from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as most recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)