import math
from time import time
from random import randint, random

from src.jether_exercise.polygon import Polygon


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


def reg_pol_area(sides, radius=1):
    side_len = math.sin(math.radians(180 / sides)) * radius * 2
    apothem = math.cos(math.radians(180 / sides)) * radius
    area = side_len * sides * apothem / 2
    return area


def test_new_polygon():
    p = Polygon()
    assert len(p) == 0


def test_iterating_over_points():
    pts = [(7, 1), (16, 6), (11, 14), (3, 9)]
    p = Polygon()

    for i, pt in enumerate(pts):
        p.insert(pt, i)

    for i, pt in enumerate(p):
        assert pt is pts[i]


def test_adding_2_points():
    p = Polygon()
    p.insert((0, 0), 0)
    p.insert((0, 5), 1)
    assert p.area() == -1


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


def test_cross():
    # all edges are the same length and angles are 90/270
    # making sure we don't count this as a regular polygon
    p = Polygon()
    pts = [(22.034284, 37.421484),
           (26.526619, 39.616691),
           (24.331412, 44.109025),
           (19.839078, 41.913819),
           (17.643871, 46.406153),
           (13.151537, 44.210947),
           (15.346743, 39.718612),
           (10.854409, 37.523406),
           (13.049615, 33.031071),
           (17.54195, 35.226278),
           (19.737156, 30.733943),
           (24.22949, 32.92915)]

    for i, pt in enumerate(pts):
        p.insert(pt, i)

    assert p.area() == -1


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

    assert p[5] == (20, 4)
    assert len(p) == 6


def test_adding_removing_and_editing_points():
    p = Polygon()
    for i, pt in enumerate(reg_polygon_helper(5)):
        p.insert(pt, i)
    assert math.isclose(p.area(), reg_pol_area(5), abs_tol=0.4)

    original_pt = p[3]
    p[3] = (30, 30)
    assert p.area() == -1

    p[3] = original_pt
    assert math.isclose(p.area(), reg_pol_area(5), abs_tol=0.4)

    p.remove(3)
    assert p.area() == -1

    p.insert(original_pt, 3)
    assert math.isclose(p.area(), reg_pol_area(5), abs_tol=0.4)


def test_area_running_time():
    p = Polygon()
    total_area_calc_time = 0
    for i, pt in enumerate(reg_polygon_helper(10000, 80)):
        p.insert(pt, i)
        t1 = time()
        area = p.area()
        total_area_calc_time += time() - t1
    assert math.isclose(area, reg_pol_area(10000, 80), abs_tol=0.4)

    assert total_area_calc_time < 0.1


def test_large_polygon():
    p = Polygon()
    for i, pt in enumerate(reg_polygon_helper(10000, 80)):
        p.insert(pt, i)
    assert math.isclose(p.area(), reg_pol_area(10000, 80), abs_tol=0.4)


if __name__ == '__main__':
    pass
    # test_rotated_square()
    # test_regular_polygons()
    test_area_running_time()
