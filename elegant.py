"""
Based on Matthew Szudzik's Elegant Pairing
http://szudzik.com/ElegantPairing.pdf
Assigns consecutive numbers to points along the edges of squares.
"""
import gmpy2


def pair(x: int, y: int) -> int:
    assert x >= 0
    assert y >= 0
    if x == max(x, y):
        z: int = gmpy2.square(x) + x + y
    else:
        z: int = gmpy2.square(y) + x
    return z


def unpair(z: int) -> (int, int):
    assert z >= 0
    x: int = z - gmpy2.square(gmpy2.isqrt(z))
    w: int = gmpy2.isqrt(z)
    if x < w:
        return x, w
    else:
        y: int = x - w
        return w, y
