class PolygonIndexError(Exception):
    def __init__(self, ind):
        self.message = f'Polygon index at: {ind} out of range'
        super().__init__(self.message)


class Node:
    def __init__(self, pt):
        self.pt = pt
        self.next = None
        self.prev = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.pt
            self.current = self.current.next
            return item

    # is there also prev?


class Polygon:
    # todo support adding points when initiating the class
    def __init__(self):
        self.__head = None
        # self.__tail = None - maybe use this later for improved performance
        self.__points = []
        self.__total_points = 0

    def insert(self, new_pt, ind):
        # if this is the first element init the head with the element
        # for now not doing checks that the index exists
        # probably should add logic that if index is too high add to the end
        new_node = Node(new_pt)
        if self.__head == None:
            curr_node = new_node
        else:
            curr_node = self.__head
        # todo - add check for if we're outside the scope of the list
        for _ in range(ind - 1):
            curr_node = curr_node.next

        next_node = curr_node.next
        if ind == 0:
            curr_node.prev = new_node
            # if it's not the first element
            if self.__head:
                new_node.next = curr_node
            self.__head = new_node
        else:
            curr_node.next = new_node
            new_node.prev = curr_node
            if next_node is not None:
                new_node.next = next_node
                next_node.prev = new_node

        self.__total_points += 1

    def remove(self, ind):
        self.__points.pop(ind)
        self.__total_points -= 1

    def __setitem__(self, ind, new_pt):
        try:
            # todo - handle exceptions and the like - if we're trying to add to an index that doesn't exist, if it's the first time we try to add
            curr_node = self.__head
            for _ in range(ind):
                curr_node = curr_node.next
            curr_node.pt = new_pt
        except:
            # this is not consistent with some of the other errors I raise
            raise PolygonIndexError(ind)

    def __getitem__(self, ind):
        return self.__points[ind]

    def __len__(self):
        return self.__total_points

    def __iter__(self):
        return LinkedListIterator(self.__head)


p = Polygon()

p.insert((0, 0), 0)
p.insert((5, 2), 1)
p.insert((10, 8), 2)
p.insert((20, 2), 3)
p.insert((5, 8), 0)
p.insert((7, 14), 0)
p.insert((8, 88), 6)
p.insert((8, 9), 7)
p[0] = (20, 14)
for pt in p:
    print(pt)

# print(a[1])
# print(a[0])
# print(a[100])
