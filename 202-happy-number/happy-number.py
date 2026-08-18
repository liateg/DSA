class Solution:
    def isHappy(self, n: int) -> bool:
        n=str(n)
        s=0
        seen=set()


        while s!=1:
                s=0
                for i in n:
                    s+=(int(i)**2)
                n=str(s)
                if s in seen:
                    return False
                seen.add(s)
                

        return True

