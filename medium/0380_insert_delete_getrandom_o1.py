import random

class RandomizedSet:

    def __init__(self):
        self.value_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.value_to_index:
            return False
        self.value_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_index:
            return False
        index = self.value_to_index[val]
        length = len(self.values)
        # Swap with the last element then remove.
        if index != length - 1:
            last = self.values[-1]
            self.values[index] = last
            self.values[-1] = val
            self.value_to_index[last] = index
            self.value_to_index[val] = length - 1
        self.value_to_index.pop(val)
        self.values.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
