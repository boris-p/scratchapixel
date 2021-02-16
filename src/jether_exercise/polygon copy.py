class PolygonIndexError(Exception):
    def __init__(self, ind):
        self.message = f'Polygon index at: {ind} out of range'
        super().__init__(self.message)


class Node:
    def __init__(self, pt):
        self.pt = pt
        self.next = None
        self.prev = None


class Polygon:
    # todo support adding points when initiating the class
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__points = []

    def insert(self, new_pt, ind=None):
        # if index is not provided insert point at the end
        if not ind:
            ind = len(self.__points)
        # currently inserts at the index if it exists and appends to the end if index does not exist
        self.__points.insert(ind, new_pt)

    def remove(self, ind):
        # todo - handle removing form an index that doesn't exist
        self.__points.pop(ind)

    def __setitem__(self, ind, new_pt):
        try:
            self.__points[ind] = new_pt
        except:
            # this is not consistent with some of the other errors I raise
            raise PolygonIndexError(ind)

    def __getitem__(self, ind):
        return self.__points[ind]

    def __len__(self):
        return len(self.__points)


p = Polygon()

p.insert((0, 0))
p.insert((5, 2))
p.insert((10, 8))
p[0] = (20, 14)
for pt in p:
    pt = (1, 1)
    print(pt)

# print(a[1])
# print(a[0])
# print(a[100])
