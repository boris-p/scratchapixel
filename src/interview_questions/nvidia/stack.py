# according to what I remember a stack is a lifo DS
# where each element has


class Item:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None


class Stack:

    def __init__(self) -> None:
        self.last = None

    def add(self, element):
        if self.last is None:
            self.last = element

        else:
            previous_last = self.last
            self.last = element
            element.prev = previous_last

    def pop(self):
        if self.last is None:
            return None

        last = self.last
        self.last = last.prev
        last.prev = None
        return last.val


s = Stack()

s.add(Item('first item'))
s.add(Item('second item'))
s.add(Item('third item'))

assert s.pop() == 'third item'
assert s.pop() == 'second item'
assert s.pop() == 'first item'
assert s.pop() == None

s.add(Item('fourth item'))
assert s.pop() == 'fourth item'


class StackAsArr:

    def __init__(self) -> None:
        self.arr = []

    def add(self, element):
        self.arr.append(element)

    def pop(self):
        if len(self.arr) == 0:
            return None
        self.arr.pop(0)
        pass


s1 = Stack()

s1.add(Item('first item'))
s1.add(Item('second item'))
s1.add(Item('third item'))

assert s1.pop() == 'third item'
assert s1.pop() == 'second item'
assert s1.pop() == 'first item'
assert s1.pop() == None

s1.add(Item('fourth item'))
assert s1.pop() == 'fourth item'
