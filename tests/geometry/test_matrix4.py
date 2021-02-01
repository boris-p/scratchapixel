from __future__ import annotations

from src.geometry.Matrix4 import Matrix4


def test_create_matrix4():
    m = Matrix4()
    assert m.m == Matrix4.IDENTITY_MATRIX


def test_multiply_identity_matrix4():
    m1 = Matrix4()
    m2 = Matrix4()
    res_m = m1.multiply(m2)

    assert res_m.m == Matrix4.IDENTITY_MATRIX


def test_transpose_identity_matrix4():
    m1 = Matrix4()
    res_m = m1.transpose()

    assert res_m.m == Matrix4.IDENTITY_MATRIX


def test_transpose_matrix4():
    m1 = Matrix4()
    m1.m = [
        [2, 4, 3, 0],
        [5, 9, 2, 6],
        [1, 8, 8, 7],
        [6, 7, 3, 1]
    ]
    res_m = m1.transpose()

    assert res_m.m == [
        [2, 5, 1, 6],
        [4, 9, 8, 7],
        [3, 2, 8, 3],
        [0, 6, 7, 1]
    ]
