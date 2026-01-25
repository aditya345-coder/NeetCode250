# Link: https://leetcode.com/problems/design-hashset/description/

"""Problem Description:
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""

# Solution: T.C: O(1), S.C: O(n)
class MyHashSet:

    def __init__(self):
        self.hashset=[]

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Alternate Solution: T.C: O(1), S.C: O(10001)
class MyHashSet:

    def __init__(self):
        self.hashset=[False]*1000001

    def add(self, key: int) -> None:
        self.hashset[key]=True

    def remove(self, key: int) -> None:
        self.hashset[key]=False

    def contains(self, key: int) -> bool:
        return self.hashset[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)




