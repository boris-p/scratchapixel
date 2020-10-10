#import pytest

from src.geometry.Vector3 import Vector3


def test_create_vector():
    vec = Vector3(0, 0, 0)
    assert vec.x == 0
