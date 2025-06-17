class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
                vector<int> answer;

    for(int i=0;i<nums.size();i++){
        for(int j=i+1;j<nums.size();j++){
            if(nums.at(i)+nums.at(j)==target){
                answer.push_back(i);
                answer.push_back(j);
               
                return answer;
            };
        };
       
            };
             return answer;
    };
   
};