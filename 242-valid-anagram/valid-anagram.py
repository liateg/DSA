class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_={}
        t_={}
        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            if s[i] in s_:
                s_[s[i]]=s_[s[i]]+1
            else:
                s_[s[i]]=1

            
        for i in range(len(t)):
            if t[i] in t_:
                t_[t[i]]=t_[t[i]]+1
            else:
                t_[t[i]]=1

        for i in s_:
            if i not in t_ or s_[i]!=t_[i]:
                return False
        return True