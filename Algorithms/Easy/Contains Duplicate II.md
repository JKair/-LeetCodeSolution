Contains Duplicate II
==========
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

这道题是`Contains Duplicate`的扩展，让我们寻找有没有两个相同的数，距离是小于k的。

解法：我们可以通过建立字典去处理这道题，字典的第一个字符代表数，第二个代表位置，每次找到相同的就判断位置的距离。

```
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> flag;
        for (int i = 0; i < nums.size(); i++) {
            if (flag.find(nums[i]) != flag.end() && i - flag[nums[i]] <= k) return true;
            else flag[nums[i]] = i;
        }

        return false;
    }
};
```

相似题目[Contains Duplicate](./Contains Duplicate.md)
