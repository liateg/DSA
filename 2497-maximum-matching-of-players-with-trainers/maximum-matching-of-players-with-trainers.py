class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        t=len(trainers)-1
        p=len(players)-1
        c=0
        players.sort()
        trainers.sort()

        while t>=0 and p>=0:
            if players[p]>trainers[t]:
                p-=1
            else:
                c+=1
                t-=1
                p-=1
        return c