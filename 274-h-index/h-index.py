class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        high = max(citations)
        size = len(citations)
        if size==1 and citations[0]>0:
            return 1
        elif size==1 and citations[0]==0:
            return 0
    # Fix: Size must be high + 1
        count = [0] * (high + 1) 
        opt = [0] * size

        for i in citations:
            count[i] += 1
    
    # Fix: Range must include the high index
        for i in range(1, high + 1):
            count[i] += count[i - 1]
    
        for i in range(size - 1, -1, -1):
            n = citations[i]
            opt[count[n] - 1] = n
            count[n] -= 1
        opt[:]=opt[::-1]

        for i in range(size):
            if i+1>opt[i]:
                return i
        return size


    