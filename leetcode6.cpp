#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <climits>
#include <map>
#include <set>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums){
        sort(nums.begin(),nums.end());
        vector<vector<int>> res;
        int n = nums.size();
        for(int i=0;i<nums.size()-2;i++){
            if(i>0 && nums[i]==nums[i-1]) continue;
            if(nums[i]>0) break;
            int left = i + 1, right = n -1 ;
            while(left<right){
                int sum = nums[i]+nums[left]+nums[right];
                if(sum == 0){
                    res.push_back({nums[i],nums[left],nums[right]});
                    while(left<right && nums[left]==nums[left+1]) left++;
                    while(left<right && nums [right] ==nums [right-1]) right--;
                    left++;
                    right--;
                }
                else if( sum <0){
                    left++;
                }
                else{
                    right --;
                }
            }
            }
            return res;
        }
    };

int main() {
    Solution solution;
    
    // 测试用例
    // 根据题目要求进行输入处理
    
    return 0;
}