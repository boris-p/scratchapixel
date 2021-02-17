import math
from random import randint, random

from src.jether_exercise.polygon import Polygon
from src.jether_exercise.polygon import approximate


def reg_polygon_helper(sides, radius=1, rotation=0, translation=None):
    one_segment = math.pi * 2 / sides

    points = [
        (math.sin(one_segment * i + rotation) * radius,
         math.cos(one_segment * i + rotation) * radius)
        for i in range(sides)]

    if translation:
        points = [[sum(pair) for pair in zip(point, translation)]
                  for point in points]

    return points


def reg_pol_area(sides, radius):
    side_len = math.sin(math.radians(180 / sides)) * radius * 2
    apothem = math.cos(math.radians(180 / sides)) * radius
    area = side_len * sides * apothem / 2
    return area


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
        assert math.isclose(p.area(), i * i, abs_tol=0.4)


def test_squares_reverse():

    for i in range(8, 2):
        p = Polygon()
        p.insert((0, 0), 0)
        p.insert((i, 0), 1)
        p.insert((i, i), 2)
        p.insert((0, i), 3)
        assert math.isclose(p.area(), i * i, abs_tol=0.4)


def test_rotated_square():
    len = 9.599248
    pts = [(7.90672097690904, 1.32498245471034), (16.2736390220239, 6.03032474762761),
           (11.5682967291067, 14.3972427927425), (3.20137868399177, 9.69190049982523)]
    p = Polygon()

    for i, pt in enumerate(pts):
        p.insert(pt, i)

    assert math.isclose(p.area(), len * len, abs_tol=0.4)


def test_rectangle_does_not_return_area():
    p = Polygon()
    p.insert((0, 0), 0)
    p.insert((0, 5), 1)
    p.insert((5, 12), 2)
    p.insert((0, 12), 3)

    assert p.area() == -1


def test_2points():
    p = Polygon()
    p.insert((0, 0), 0)
    p.insert((0, 5), 1)
    assert p.area() == -1


def test_square():
    p = Polygon()
    for i, pt in enumerate(reg_polygon_helper(4, 80)):
        p.insert(pt, i)
    assert math.isclose(p.area(), reg_pol_area(4, 80), abs_tol=0.4)


def test_pentagon():
    p = Polygon()
    for i, pt in enumerate(reg_polygon_helper(5, 80)):
        p.insert(pt, i)
    assert math.isclose(p.area(), reg_pol_area(5, 80), abs_tol=0.4)


def test_rotated_translated_pentagon():
    p = Polygon()
    for i, pt in enumerate(reg_polygon_helper(5, 80, -0.3, (43, 2))):
        p.insert(pt, i)
    assert math.isclose(p.area(), reg_pol_area(5, 80), abs_tol=0.4)


def test_many_polygons():
    for i in range(3, 100):
        p = Polygon()
        radius = randint(1, 300)
        x_trans = randint(100, 200)
        y_trans = randint(200, 400)
        for j, pt in enumerate(reg_polygon_helper(i, radius, random(), (x_trans, y_trans))):
            p.insert(pt, j)
        assert math.isclose(p.area(), reg_pol_area(i, radius), abs_tol=0.4)


def test_update_point():
    p = Polygon()
    for i, pt in enumerate(reg_polygon_helper(5, 80)):
        p.insert(pt, i)
    assert math.isclose(p.area(), reg_pol_area(5, 80), abs_tol=0.4)

    # random point - check that polygon is no longer regular
    p.insert((20, 4), 5)
    assert p.area() == -1

    assert p[5] is (20, 4)
    assert len(p) == 6


def test_large_polygon():
    p = Polygon()
    for i, pt in enumerate(reg_polygon_helper(10000, 80)):
        p.insert(pt, i)
    assert math.isclose(p.area(), reg_pol_area(10000, 80), abs_tol=0.4)


if __name__ == '__main__':
    pass
    # test_rotated_square()
    # test_regular_polygons()
