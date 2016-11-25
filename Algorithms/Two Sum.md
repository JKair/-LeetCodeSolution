Two Sum
==========
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

这道题要我们在一个数组里面，找出两个数，相加等于第二个参数，返回那两个数的下标，这里有两种解法。

第一种，解法就是直接遍历，第一层用一个变量去记录减去当前变量后要找的那个变量，然后在第二层循环找，找到了就返回。注意，直接暴力搜索肯定是不能过的！但是找到了就返回，优化了暴力搜索需要跑遍所有情况的尴尬，所以这种解法是可以过的。解法如下：
```
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            int temp = target - nums[i];
            for (int j = i+1 ; j < nums.size(); j++) {
                if (nums[j] == temp) {
                    return {i,j};
                }
            }
        }

        return {};
    }
};
```

第二种解法，用map记录每个数字的的下标索引，时间复杂度是O(N)，解法优雅很多。

```
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> temp;
        for (int i = 0; i < nums.size(); i++) {
            temp[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int flag = target - nums[i];
            if (temp.count(flag) && temp[flag] != i) {
                return {i, temp[flag]};
            }
        }

        return {};
    }
};
```

相似题目：[3Sum](./3Sum.md)、[3Sum Closest](./3Sum Closest.md)、[4Sum](./4Sum.md)
