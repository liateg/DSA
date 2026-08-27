class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        pre={
            '(':')',
            '{':'}',
            '[':']'
        }
        close=[]
        for p in s:
            if p in pre:
                close.append(pre[p])
            else:
                
                if len(close)!=0 and p== close[-1]:
                    close.pop()
                else:
                    return False
        return (len(close)==0)

