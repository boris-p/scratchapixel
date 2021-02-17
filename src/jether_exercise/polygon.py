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
    # TODO support adding points when initiating the class
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__total_points = 0

        # we cache the area and flush the cash anytime a point changes
        # so that we perform the area calculation only once per a set amount of points
        self.__area = None

        # a dictionary that holds the length of each edge and number of occurrences
        # used in checks for a regular polygon
        self.__edges_len = dict()

        # a dictionary that holds the angles of the polygon and number of occurrences
        # used in checks for a regular polygon
        self.__angles = dict()

        # checking the convexity of polygon - used for checking the polygon is regular
        self.__z_product_pos = 0
        self.__z_product_neg = 0

    def insert(self, new_pt, ind):

        self.__area = None
        # if this is the first element init the head with the element
        # for now not doing checks that the index exists
        # probably should add logic that if index is too high add to the end
        new_node = Node(new_pt)

        # first node
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
            self.__total_points += 1
            return

        # adding last node
        if ind >= self.__total_points:
            last_node = self.__tail
            last_node.next = new_node
            new_node.prev = last_node
            self.__tail = new_node
        else:
            curr_node = self.__head
            for _ in range(ind):
                curr_node = curr_node.next

            prev_node = curr_node.prev
            if prev_node:
                prev_node.next = new_node
                new_node.prev = prev_node
            else:
                self.__head = new_node

            curr_node.prev = new_node
            new_node.next = curr_node

        self.__total_points += 1

        # not a polygon just yet
        if self.__total_points < 3:
            return

        # update local polygon values for checking if a polygon is regular
        e = new_node
        b = self.__prev(e)
        a = self.__prev(b)
        c = self.__next(e)
        d = self.__next(c)

        self.__angle_and_zproduct(a, b, e, 'add')
        self.__angle_and_zproduct(b, e, c, 'add')
        self.__angle_and_zproduct(e, c, d, 'add')
        self.__edge_len(b, e, 'add')
        self.__edge_len(e, c, 'add')

        if self.__total_points == 3:
            self.__edge_len(c, d, 'add')
        else:
            self.__angle_and_zproduct(a, b, c, 'remove')
            self.__angle_and_zproduct(b, c, d, 'remove')
            self.__edge_len(b, c, 'remove')

    def remove(self, ind):
        self.__area = None

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

        # update local polygon values for checking if a polygon is regular
        if self.__total_points < 3:
            # reset area calculation stores
            self.__edges_len = dict()
            self.__angles = dict()
            self.__z_product_pos = 0
            self.__z_product_neg = 0
            return

        e = curr_node
        b = self.__prev(e)
        a = self.__prev(b)
        c = self.__next(e)
        d = self.__next(c)

        self.__angle_and_zproduct(a, b, e, 'remove')
        self.__angle_and_zproduct(b, e, c, 'remove')
        self.__angle_and_zproduct(e, c, d, 'remove')
        self.__edge_len(b, e, 'remove')
        self.__edge_len(e, c, 'remove')

        self.__angle_and_zproduct(a, b, c, 'add')
        self.__angle_and_zproduct(b, c, d, 'add')
        self.__edge_len(b, c, 'add')

    def area(self):
        # we clear the area every time a mutation to the polygon occurs
        # if we have an area it means it was asked before and no change
        # to the oplygon was done
        if self.__area:
            return self.__area

        # we consider the polygon regular if all angles are the same size
        # edges have the same length and it is convex
        if max(self.__z_product_neg, self.__z_product_pos) == self.__total_points and \
                len(self.__edges_len) == 1 and len(self.__angles) == 1:

            side_len, sides = [*self.__edges_len.items()][0]
            apothem = side_len / (2 * (math.tan(math.radians(180 / sides))))

            area = side_len * sides * apothem / 2
            self.__area = area
            return area
        else:
            self.__area = None
            return -1

    # get prev node (if index is 0 return the last)
    def __prev(self, node):
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
        self.__area = None
        if ind >= self.__total_points:
            raise PolygonIndexError(ind)

        curr_node = self.__head
        for _ in range(ind):
            curr_node = curr_node.next

        old_node = Node(curr_node.pt)
        curr_node.pt = new_pt

        if self.__total_points < 3:
            return

        # update local polygon values for checking if a polygon is regular
        e = curr_node
        b = self.__prev(e)
        a = self.__prev(b)
        c = self.__next(e)
        d = self.__next(c)
        self.__edge_len(b, old_node, 'remove')
        self.__edge_len(old_node, c, 'remove')
        self.__edge_len(b, e, 'add')
        self.__edge_len(e, c, 'add')

        self.__angle_and_zproduct(a, b, old_node, 'remove')
        self.__angle_and_zproduct(b, old_node, c, 'remove')
        self.__angle_and_zproduct(old_node, c, d, 'remove')
        self.__angle_and_zproduct(a, b, e, 'add')
        self.__angle_and_zproduct(b, e, c, 'add')
        self.__angle_and_zproduct(e, c, d, 'add')

    def __getitem__(self, ind):
        # TODO - support negative values to access from the end
        curr_node = self.__head

        if not curr_node or ind >= self.__total_points:
            raise PolygonIndexError(ind)
        for _ in range(ind):
            curr_node = curr_node.next
        return curr_node.pt

    def __len__(self):
        return self.__total_points

    def __iter__(self):
        return LinkedListIterator(self.__head)
