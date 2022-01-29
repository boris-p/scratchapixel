# fifo queues implementation

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class QueueAsLinkList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = Node(val)
        if self.head:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def walk(self):
        print("walking queue as link list")
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def walk_back(self):
        print("walking queue as link list backwards")
        curr = self.tail
        while curr:
            print(curr.val)
            curr = curr.prev

    def pop(self):
        curr = self.tail
        if curr:
            print(f"popping {self.tail.val}")
            if curr.prev:
                self.tail = curr.prev
                self.tail.next = None
                return self.tail
            else:
                self.head = None
                self.tail = None
                return None
        else:
            print("no elements in the queue")
            return None


queue_as_linked_list = QueueAsLinkList()

queue_as_linked_list.push(2)
queue_as_linked_list.push(54)
queue_as_linked_list.push(87)
queue_as_linked_list.push(21)
queue_as_linked_list.push(90)
queue_as_linked_list.walk()
queue_as_linked_list.walk_back()
queue_as_linked_list.pop()
queue_as_linked_list.pop()
queue_as_linked_list.pop()
queue_as_linked_list.pop()
queue_as_linked_list.pop()
queue_as_linked_list.pop()
queue_as_linked_list.pop()
queue_as_linked_list.pop()
queue_as_linked_list.walk()
