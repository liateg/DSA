class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # re arange 
        sorted_={}
        
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in sorted_:
                sorted_["".join(sorted(strs[i]))].append(i)
            else: 
                sorted_["".join(sorted(strs[i]))]=[i]
        newg=[]
        for i in sorted_:
            mini=[]
            for j in range(len(sorted_[i])):
                mini.append(strs[sorted_[i][j]])
            newg.append(mini)
            
        return newg
           



        
   


            