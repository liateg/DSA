class Solution: 
    def selectionSort(self, arr):
        # code here
    
        for i in range(len(arr)):
            miin=i
            for j in range(i,len(arr)):
                if arr[miin]>arr[j]:
                    miin=j
            arr[miin],arr[i]=arr[i],arr[miin]
        return arr
