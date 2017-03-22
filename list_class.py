import collections

class My_List:
    def __init__(self, lst):
        self._lst = lst

    def __getitem__(self, item):
        return self._lst[item]

    def __str__(self):
        return str(self._lst)

    # A method to return all unique items from the list
    def unique(self):
        return set(self)

    # A method to append new items to the list
    def append(self, item):
         self._lst.append(item)

    # A method to insert new items into the list
    def insert(self, position, item):
        return self._lst.insert(position, item)

    # A method to return all items and their frequency
    def all_items(self):
        counter = collections.Counter(self)
        return counter
