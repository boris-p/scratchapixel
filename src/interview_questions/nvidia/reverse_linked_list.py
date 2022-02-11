class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val: int):
        if not self.head:
            self.head = Node(val)
            return
        curr_node = self.head

        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(val)

    def find(self, val):
        curr_node = self.head
        while curr_node:
            if curr_node.val == val:
                print(f'found {val}')
                return
            curr_node = curr_node.next
        print(f"could not find {val}")

    def delete(self, val):
        curr_node = self.head
        prev = None
        while curr_node:
            if curr_node.val == val:
                print(f'deleting {val}')
                # deleting root element
                if not prev:
                    self.head = curr_node.next
                else:
                    prev.next = curr_node.next
                return
            else:
                prev = curr_node
                curr_node = curr_node.next
        print(f"could not find and delete {val}")

    def walk(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.val)
            curr_node = curr_node.next

    def reverse(self):
        prev = self.head
        curr = prev.next
        prev.next = None
        if curr is None:
            return

        while True:
            next = curr.next
            curr.next = prev
            if next is None:
                self.head = curr
                break

            prev = curr
            curr = next


list = LinkedList()
list.append(1)
list.append(5)
list.append(88)
list.append(3)
list.append(12)

# list.walk()
list.reverse()

list.walk()
