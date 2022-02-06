# according to what I remember a queue is a fifo DS
# where each element has


class Item:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None


class Queue:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, element):
        if self.tail is None:
            self.tail = element
            self.head = element
        else:
            previous_prev = self.tail
            self.tail = element
            previous_prev.prev = element

    def pop(self):
        if self.head is None:
            return None

        previous_head = self.head

        if previous_head.prev is None:
            self.head = None
            self.tail = None
        else:
            self.head = previous_head.prev

        previous_head.prev = None
        return previous_head.val


q = Queue()

q.add(Item('first item'))
q.add(Item('second item'))
q.add(Item('third item'))

assert q.pop() == 'first item'
assert q.pop() == 'second item'
assert q.pop() == 'third item'
assert q.pop() == None

q.add(Item('fourth item'))
assert q.pop() == 'fourth item'


class QueueAsArr:

    def __init(self) -> None:
        self.arr = []

    def add(self, element):
        self.arr.append(element)

    def pop(self):
        if len(self.arr) == 0:
            return None
        self.arr.pop()
        pass


q1 = Queue()

q1.add(Item('first item'))
q1.add(Item('second item'))
q1.add(Item('third item'))

assert q1.pop() == 'first item'
assert q1.pop() == 'second item'
assert q1.pop() == 'third item'
assert q1.pop() == None

q1.add(Item('fourth item'))
assert q1.pop() == 'fourth item'
