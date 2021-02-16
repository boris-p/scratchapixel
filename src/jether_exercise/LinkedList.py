class Node:
    def __init__(self, pt):
        self.pt = pt
        self.next = None
        self.prev = None


class LintedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, pt):
        n = Node(pt)
        # first element
        if self.head == None:
            self.head = n
            self.tail = n
        # not first element
        else:
            h = self.tail
            h.next = n
            n.prev = h
            self.tail = n

    def delete(self, value):
        print("hello world1")

    def find(self, value):
        print("hello world1")
