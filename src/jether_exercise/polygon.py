import math


ROUND_DECIMALS = 10 ** 6


class PolygonIndexError(Exception):
    def __init__(self, ind):
        self.message = f'Polygon index at: {ind} out of range'
        super().__init__(self.message)


class PolygonRemoveIndexError(Exception):
    def __init__(self, ind, len):
        self.message = f'trying to remove element with index {ind} from a polygon with length {len}'
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


# approximate angle and edge length calculations to avoid precision errors
def approximate(num):
    return round(num * ROUND_DECIMALS) / ROUND_DECIMALS


class Polygon:
    # todo support adding points when initiating the class
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__total_points = 0

        # a dictionary that holds the length of each edge and number of occurrences
        # used in checks for a regular polygon
        self.__edges_len = dict()

        # a dictionary that holds the angles of the polygon and number of occurrences
        # used in checks for a regular polygon
        self.__angles = dict()

        self.__z_product_pos = 0
        self.__z_product_neg = 0
        # TODO - don't forget to cache the value of the area and if it's a right polygon

    def insert(self, new_pt, ind):
        # if this is the first element init the head with the element
        # for now not doing checks that the index exists
        # probably should add logic that if index is too high add to the end
        new_node = Node(new_pt)
        if self.__head == None:
            curr_node = new_node  # this should be called head, no?
        else:
            curr_node = self.__head
        # todo - add check for if we're outside the scope of the list
        for _ in range(ind - 1):
            curr_node = curr_node.next

        next_node = curr_node.next

        if ind == self.__total_points:
            self.__tail = new_node
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

        # not a polygon just yet
        if self.__total_points < 3:
            return

        # update local polygon values for checking is a polygon is regular
        if self.__total_points == 3:
            # TODO - make this more concise
            c = new_node
            a = self.__next(c)
            b = self.__prev(c)
            self.__angle_and_zproduct(a, b, c, 'add')
            self.__angle_and_zproduct(b, c, a, 'add')
            self.__angle_and_zproduct(c, a, b, 'add')

            self.__edge_len(a, b, 'add')
            self.__edge_len(b, c, 'add')
            self.__edge_len(c, a, 'add')
        else:
            e = new_node
            b = self.__prev(new_node)
            a = self.__prev(b)
            c = self.__next(new_node)
            d = self.__next(c)

            self.__angle_and_zproduct(a, b, c, 'remove')
            self.__angle_and_zproduct(b, c, d, 'remove')
            self.__edge_len(b, c, 'remove')

            self.__angle_and_zproduct(a, b, e, 'add')
            self.__angle_and_zproduct(b, e, c, 'add')
            self.__angle_and_zproduct(e, c, d, 'add')
            self.__edge_len(b, e, 'add')
            self.__edge_len(e, c, 'add')

    def remove(self, ind):

        if ind >= self.__total_points:
            raise PolygonRemoveIndexError(ind, self.__total_points)
        curr_node = self.__head
        for _ in range(ind):
            curr_node = curr_node.next

        if curr_node.prev:
            curr_node.prev.next = curr_node.next
        else:
            # first node - update head
            self.__head = curr_node.next

        if curr_node.next:
            curr_node.next.prev = curr_node.prev
        else:
            # last node - update tail
            self.__tail = curr_node.prev

        self.__total_points -= 1

        # update local polygon values for checking is a polygon is regular

    def area(self):
        # we consider the polygon regular if all angles are the same size
        # edges have the same length and its convex
        if max(self.__z_product_neg, self.__z_product_pos) == self.__total_points and \
                len(self.__edges_len) == 1 and len(self.__angles) == 1:

            side_len, sides = [*self.__edges_len.items()][0]
            apothem = side_len / (2 * (math.tan(math.radians(180 / sides))))

            # todo - don't forget to cache the area
            area = side_len * sides * apothem / 2
            return area
        else:
            return -1

    # get prev node (if index is 0 return the last)
    def __prev(self, node):
        # todo - support prev prev (number of steps)
        return node.prev if node.prev else self.__tail

    # get next node (if node is last return the first)
    def __next(self, node):
        return node.next if node.next else self.__head

    def __angle_and_zproduct(self, _a, _b, _c, operation):
        a = _a.pt
        b = _b.pt
        c = _c.pt
        ang = math.degrees(math.atan2(
            c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
        ang = ang + 360 if ang < 0 else ang
        ang = approximate(ang)

        z_cross_product_pos = ((a[0]-b[0])*(b[1]-c[1]) -
                               (a[1]-b[1])*(b[0]-c[0]) > 0)

        if operation == 'add':
            if z_cross_product_pos is True:
                self.__z_product_pos += 1
            else:
                self.__z_product_neg += 1

            self.__angles[ang] = self.__angles[ang] + \
                1 if self.__angles.get(ang) else 1

        elif operation == 'remove':
            if z_cross_product_pos is True:
                self.__z_product_pos -= 1
            else:
                self.__z_product_neg -= 1

            self.__angles[ang] -= 1
            if self.__angles[ang] == 0:
                del self.__angles[ang]

    def __edge_len(self, _a, _b, operation):
        a = _a.pt
        b = _b.pt
        edge = approximate(math.dist(a, b))
        if operation == 'add':
            self.__edges_len[edge] = self.__edges_len[edge] + \
                1 if self.__edges_len.get(edge) else 1

        elif operation == 'remove':
            self.__edges_len[edge] -= 1
            if self.__edges_len[edge] == 0:
                del self.__edges_len[edge]

    def __setitem__(self, ind, new_pt):
        try:
            # todo - handle exceptions and the like - if we're trying to add to an index that doesn't exist, if it's the first time we try to add
            curr_node = self.__head
            for _ in range(ind):
                curr_node = curr_node.next
            curr_node.pt = new_pt
        except:
            raise PolygonIndexError(ind)

    def __getitem__(self, ind):
        # TODO - support negative values to access from the end
        # TODO - i'm not handling errors well
        curr_node = self.__head
        for _ in range(ind):
            curr_node = curr_node.next
        return curr_node.pt

    def __len__(self):
        return self.__total_points

    def __iter__(self):
        return LinkedListIterator(self.__head)
