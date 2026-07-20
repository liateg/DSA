from math import gcd, isqrt

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        gcd_ = gcd(a, b)
        c = 0

        for i in range(1, isqrt(gcd_) + 1):
            if gcd_ % i == 0:
                if gcd_ // i == i:
                    c += 1
                else:
                    c += 2

        return c