import math


from src.jether_exercise.polygon import Polygon
from src.jether_exercise.polygon import approximate


def test_new_polygon():
    p = Polygon()
    assert len(p) == 0


def test_squares():

    for i in range(2, 8):
        p = Polygon()
        p.insert((0, 0), 0)
        p.insert((i, 0), 1)
        p.insert((i, i), 2)
        p.insert((0, i), 3)

        assert p.area() == i * i


def test_squares_reverse():

    for i in range(8, 2):
        p = Polygon()
        p.insert((0, 0), 0)
        p.insert((i, 0), 1)
        p.insert((i, i), 2)
        p.insert((0, i), 3)

        assert p.area() == i * i


def test_rotated_square():
    len = 9.599248
    pts = [(7.90672097690904, 1.32498245471034), (16.2736390220239, 6.03032474762761),
           (11.5682967291067, 14.3972427927425), (3.20137868399177, 9.69190049982523)]
    p = Polygon()

    for i, pt in enumerate(pts):
        p.insert(pt, i)

    assert p.area() == approximate(len * len)


def test_rectangle_does_not_return_area():
    p = Polygon()
    p.insert((0, 0), 0)
    p.insert((0, 5), 1)
    p.insert((5, 12), 2)
    p.insert((0, 12), 3)

    assert p.area() == -1


test_rotated_square()
