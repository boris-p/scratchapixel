from __future__ import annotations
import math

from src.geometry.Vector3 import Vector3


def test_create_vector():
    vec = Vector3(0, 0, 0)
    assert vec.x == 0


def test_duplicate():
    vec = Vector3(3, 2, 4)
    duplicate = vec.duplicate()
    vec.x = 5
    assert duplicate.x == 3
    assert vec.x == 5


def test_vector_length():
    vec = Vector3(1, 1, 1)
    assert math.isclose(vec.length(), 1.732,  abs_tol=1e-03)


def test_dot_product():
    vec = Vector3(1, 1, 1)
    vecB = Vector3(2, 2, 2)
    assert math.isclose(vec.dot(vecB), 6,  abs_tol=1e-03)


def test_angle():
    vec = Vector3(5, 7, 0)
    vecB = Vector3(2, 8, 0)
    assert math.isclose(math.degrees(vec.angle(vecB)), 21.501, abs_tol=1e-03)


def test_angle_2():
    vec = Vector3(5, 7, 0)
    vecB = Vector3(-3, -6, 0)
    assert math.isclose(math.degrees(vec.angle(vecB)), 171.027, abs_tol=1e-03)


def test_cross():
    vec = Vector3(2, 0, 0)
    vecB = Vector3(0, 2, 0)
    cross = vec.cross(vecB)
    assert cross.x == 0
    assert cross.y == 0
    assert cross.z == 4


def test_cross_negative():
    vec = Vector3(2, 0, 0)
    vecB = Vector3(0, 2, 0)
    cross = vecB.cross(vec)
    assert cross.x == 0
    assert cross.y == 0
    assert cross.z == -4


def test_cross_2():
    vec = Vector3(5, 7, 0)
    vecB = Vector3(-3, -6, 0)
    cross = vec.cross(vecB)
    assert cross.z == -9
    assert cross.x == 0
    assert cross.y == 0
