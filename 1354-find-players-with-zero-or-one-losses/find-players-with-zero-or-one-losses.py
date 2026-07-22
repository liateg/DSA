from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose = Counter()
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            lose[loser] += 1

        return [
            sorted([p for p in players if lose[p] == 0]),
            sorted([p for p in players if lose[p] == 1])
        ]