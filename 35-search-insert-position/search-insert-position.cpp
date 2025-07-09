class Solution {
public:
        int searchInsert(vector<int>& nums, int target) {
        int mid,left=0;
        int right=nums.size()-1;
    while(right>=left){
            
        mid = left + (right - left) / 2;
       if(left==right && nums.at(mid)<target){return mid+1;}
       if(left==right && nums.at(mid)>target){return mid;}

        if(nums.at(mid)==target){
            return mid;
        }
        if (nums.at(mid)<target){
            left=mid+1;
        }else{
            right=mid-1;
        }
        
    }; 
    if (mid==nums.size()-1){ return ++mid;}else{return mid;}
    
        };
    
};