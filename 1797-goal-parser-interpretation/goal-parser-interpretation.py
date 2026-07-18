class Solution:
    def interpret(self, command: str) -> str:
        i=0
        res=[]
        while i<len(command):
            if command[i]=='G':
                res.append('G')
                i+=1
            elif command[i+1]==')':
                res.append('o')
                i+=2
            elif i<len(command)-3 and command[i+3]==')':
                res.append('al')
                i+=4

        return ''.join(res)