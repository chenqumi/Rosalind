class Stack(object):
    """docstring for Stack"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        # top = len(self.items) - 1
        return self.items[-1]

    def size(self):
        return len(self.items)
        

class Queue(object):
    """docstring for Queue"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enQ(self, item):
        self.items.insert(0, item)

    def deQ(self):
        self.items.pop()

    def size(self):
        return len(self.items)

