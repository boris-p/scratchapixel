#import pytest
import math

from src.geometry.Vector3 import Vector3


def test_create_vector():
    vec = Vector3(0, 0, 0)
    assert vec.x == 0


def test_vector_length():
    vec = Vector3(1, 1, 1)
    assert math.isclose(vec.length(), 1.732,  abs_tol=1e-03)


def test_dot_product():
    vec = Vector3(1, 1, 1)
    vecB = Vector3(2, 2, 2)
    assert math.isclose(vec.dot(vecB), 6,  abs_tol=1e-03)
