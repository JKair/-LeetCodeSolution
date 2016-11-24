3Sum
=============

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

这道题让我们找出三个数加起来等于0的情况。

第一种解法，使用递归，先将数组进行排序，每次都将加的结果递给下个函数，这样就能不断的循环计算结果，满足退出的条件为，当`temp = 0 && out.size() == 3`，就是说已经凑满三个数而且三个数的结果为0，然后超时了。
```
//Time Limit Exceeded
class Solution {
public:
    void threeSum(vector<int> &nums, vector<int> &out, set<vector<int>> &res, int start, int temp) {
        if (out.size() == 3 && temp == 0) {
            res.insert(out);

            return ;
        }

        for (int i = start; i < nums.size(); i++) {
            if (temp > 0 && nums[i] > 0) {
                break;
            }
            out.push_back(nums[i]);
            threeSum(nums,out,res,i+1,temp+nums[i]);
            out.pop_back();
        }
    }

    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;
        vector<int> out;
        sort(nums.begin(), nums.end());
        threeSum(nums,out,res,0,0);
        vector<vector<int>> last(res.begin(), res.end());

        return last;
    }
};
```

第二种解法：迭代，先将数组排序，然后循环遍历，先用`0-nums[i]`，这样就可以将问题分解能2sum，用两个变量从两边分别向对方跑，当遇到满足条件的时候就直接插入就可以了，另外用set集合可以直接解决重复的问题，如果不用set，可以额外加多一个循环，将此时插入的`num[left]`和`num[right]`跳过。

使用set:
```
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int temp = 0 - nums[i], left = i + 1, right = nums.size()-1;

            while (left < right) {
                if (nums[left] + nums[right] > temp) right--;
                else if (nums[left] + nums[right] < temp) left++;
                else {
                    res.insert({nums[i],nums[left],nums[right]});
                    left++;
                    right--;
                }
            }
        }

        vector<vector<int>> last(res.begin(), res.end());

        return last;
    }
};
```
不使用：
```
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int temp = 0 - nums[i], left = i + 1, right = nums.size()-1;

            while (left < right) {
                if (nums[left] + nums[right] > temp) right--;
                else if (nums[left] + nums[right] < temp) left++;
                else {
                    res.push_back({nums[i],nums[left],nums[right]});
                    while (left < right && nums[left] == nums[left+1]) left++;
                    while (left < right && nums[right] == nums[right-1]) right--;
                    left++;
                    right--;
                }
            }
        }

        return res;
    }
};
```
