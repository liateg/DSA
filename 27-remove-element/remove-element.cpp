class Solution {
public:
int removeElement(vector<int>& nums, int val) {
    int i=0;
    while (i<nums.size()){
       if (val==nums[i]){
           nums.erase(nums.begin()+i);
       
   
          i--;
   
       };
       i++;
   
    };
    return nums.size();  
}
};