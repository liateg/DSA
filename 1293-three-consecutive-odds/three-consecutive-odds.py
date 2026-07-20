class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
         c=0
         for i in arr:
            if c>=3:
                return True
            if i%2==0:
                c=0
            else:
                c+=1
                
         return c>=3
            
