# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

class MyHashSet:

    def __init__(self):
        self.store = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.store[key] = True

    def remove(self, key: int) -> None:
        self.store[key] = False

    def contains(self, key: int) -> bool:
        return self.store[key]


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
