import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set1=set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set1:
            return False
        else:
            self.set1.add(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set1:
            self.set1.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        rand_index= random.randint(0, len(self.set1)-1)
        set_list = list(self.set1)
        return set_list[rand_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
