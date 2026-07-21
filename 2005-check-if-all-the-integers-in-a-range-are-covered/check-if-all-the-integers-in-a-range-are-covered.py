class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        new=set()

        for i in ranges:
            new.update(range(i[0],i[1]+1))
        return set(range(left, right + 1)) <= new