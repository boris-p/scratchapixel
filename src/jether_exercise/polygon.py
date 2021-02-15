
class PolygonIndexError(Exception):
    def __init__(self, ind):
        self.message = f'Polygon index at: {ind} out of range'
        super().__init__(self.message)


class Polygon:
    def __init__(self):
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
            raise PolygonIndexError(ind)

    def __getitem__(self, ind):
        return self.__points[ind]

    def __len__(self):
        return len(self.__points)


p = Polygon()

p.insert('first point')
p.insert('second point')
p.insert('third point')
p[0] = 'test'
for pt in p:
    print(pt)
# print(a[1])
# print(a[0])
# print(a[100])
