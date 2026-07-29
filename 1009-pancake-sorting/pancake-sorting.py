class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        
        

        for i in range(len(arr),1,-1):
            maxi=arr.index(max(arr[:i]))
            if maxi==i-1:
                continue
            if maxi!=0:

                arr[0:maxi+1]=arr[:maxi+1][::-1]
                ans.append(maxi+1)
            arr[:i]=arr[:i][::-1]
            ans.append(i)



            
           
        return ans