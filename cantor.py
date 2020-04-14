"""
Cauchy-Cantor “diagonal” polynomials
Assigns consecutive numbers to points along diagonals in the plane.
"""
import gmpy2


def pair(x: int, y: int) -> int:
    assert x >= 0
    assert y >= 0
    z: int = (x+y) * (x+y+1) // 2 + y
    return z


def unpair(z: int) -> (int, int):
    assert z >= 0
    w: int = (gmpy2.isqrt((8 * z) + 1) - 1) // 2
    y: int = z - (gmpy2.square(w) + w) // 2
    x: int = w - y
    return x, y
