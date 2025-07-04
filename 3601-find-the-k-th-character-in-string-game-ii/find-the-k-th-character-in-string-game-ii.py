import math
import string   # for ascii_lowercase

class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        # how many operations are even relevant
        i = math.ceil(math.log2(k)) - 1

        shift = 0         # total +1 shifts accumulated so far
        while i >= 0:
            half = 1 << i  # 2**i
            if k > half:   # k sits in the "right" half
                k -= half
                shift += operations[i]
            i -= 1

        return string.ascii_lowercase[shift % 26]
