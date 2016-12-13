4Sum
==========

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

查找四个数相加起来等于0

其实这道题只要在3Sum的基础改装下就可以ac了。


```
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        set<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size(); j++) {
                int left = j + 1, right = nums.size()-1;

                while (left < right) {
                    int sum = nums[left] + nums[right] + nums[i] + nums[j];
                    if (sum > target) right--;
                    else if (sum < target) left++;
                    else {
                        res.insert({nums[i],nums[j],nums[left],nums[right]});
                        left++;
                        right--;
                    }
                }
            }
        }
        vector<vector<int>> fuck = {res.begin(), res.end()};
        return fuck;
    }
};
```


相似题目：[Two Sum](./Two Sum.md)、[3Sum](./3Sum.md)、[3Sum Closest](./3Sum Closest.md)
