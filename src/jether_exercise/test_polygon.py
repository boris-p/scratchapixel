from src.jether_exercise.polygon import Polygon


p = Polygon()

p.insert('first point')
p.insert('second point')
p.insert('third point')
p[0] = 'test'
for pt in p:
    print(pt)


def test_new_polygon():
    p = Polygon()
    assert len(p) is 0
