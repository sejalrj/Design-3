class DLL:
    def __init__(self, key,value):
        self.next = None
        self.prev = None
        self.key = key
        self.val = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity= capacity
        self.dic = {}
        self.dllFront = DLL(None, None)
        self.dllRear = DLL(None, None)
        self.dllFront.next = self.dllRear
        self.dllRear.prev = self.dllFront

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.update(node, node.val)
            return node.val
        else:
            return -1

    def add(self, node):
        temp = self.dllFront.next
        self.dllFront.next = node
        node.next = temp
        node.prev = self.dllFront
        temp.prev = node
    

    def update(self, node, val):
        node.val = val
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add(node)

    def remove(self):
        node_to_delete = self.dllRear.prev
        node_to_delete.prev.next = self.dllRear
        self.dllRear.prev = node_to_delete.prev
        del self.dic[node_to_delete.key]

    def put(self, key: int, value: int) -> None:

        if key in self.dic:
            self.update(self.dic[key], value)
  
        else:
            if len(self.dic) == self.capacity:
                self.remove()
            newNode = DLL(key, value)
            self.add(newNode)
            self.dic[key] = newNode



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
