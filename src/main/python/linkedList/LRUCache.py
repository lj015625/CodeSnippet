from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.od = OrderedDict()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.od:
            # return nothing
            return
        # move this item to most fresh
        self.od.move_to_end(key)
        return self.od[key]

    def getMostRecentKey(self):
        return list(self.od.keys())[-1]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.od:
            # move this item to most fresh
            self.od.move_to_end(key)
        # add new item
        self.od[key] = value

        # FIFO order if false, remove the oldest item
        if len(self.od) > self.capacity:
            self.od.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
capacity = 10
obj = LRUCache(capacity)
key = 1
param_1 = obj.get(key)
print(param_1)
value = 2
obj.put(key, value)
print(obj.get(key))