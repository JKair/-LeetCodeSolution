Contains Duplicate
========
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

这道题让我们判断一个数组里面是否有重复的数字。

解法一：建立一个字典，每次都查找字典，如果字典里面没有的话，说明没出现过这个数，那么放进去，如果字典里面出现过，就直接返回true了。

```
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> res;
        for (int i = 0; i < nums.size(); i++) {
            if (res.find(nums[i]) != res.end()) return true;

            res[nums[i]]++;
        }

        return false;
    }
};
```

解法二：淫荡得不行，把vector变成set，然后判断两者的长度是否相等就可以了。

```
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return nums.size() != set<int>(nums.begin(), nums.end()).size();
    }
};
```
