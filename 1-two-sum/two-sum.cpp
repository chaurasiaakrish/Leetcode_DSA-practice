class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>mpp;

        for(int i=0;i<nums.size();i++){
            int intial=target-nums[i];
          if(mpp.find(intial)!=mpp.end()){
            return {mpp[intial],i};
        }
        mpp[nums[i]]=i;
        }
        return {};
    }
};