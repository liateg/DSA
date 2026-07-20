class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        s=0

        for i in str(x):
            s+=int(i)

        return s if x%s==0 else -1

