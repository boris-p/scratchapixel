from __future__ import annotations
import math

from src.geometry.Matrix4 import Matrix4


def test_create_matrix4():
    m = Matrix4()
    assert m.m == Matrix4.IDENTITY_MATRIX


def test_multiply_identity_matrix4():
    m1 = Matrix4()
    m2 = Matrix4()
    res_m = m1.multiply(m2)

    res_m.m = Matrix4.IDENTITY_MATRIX
