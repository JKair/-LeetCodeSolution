Remove Duplicates from Sorted Array
===================================

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

这道题让我们删除已经排序好的数组中重复的数，并返回最终的长度。

解法一：我们可以利用set的性质，将所有的数放进set，然后反过来再放进vector，最后返回size。搞定

```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> fuck;
        for (auto i:nums) {
            fuck.insert(i);
        }

        int n = nums.size();
        nums.clear();
        for (auto i:fuck) {
            nums.push_back(i);
        }

        return nums.size();
    }
};
```

解法二：我们可以创建两个变量来记录，一个是最终的长度`res`，另外一个就是上次的数`last`，当我们遇到与`last`不同的数的时候，将本次的数赋值给`res`，然后将`last`变为本次的数，这样维护完就可以得到最后没有重复的数组了

```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int res = 1, last = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != last) {
                nums[res++] = nums[i];
                last = nums[i];
            }
        }

        return res;
    }
};
```

相似题目[Remove Duplicates from Sorted Array II](./Remove Duplicates from Sorted Array II.md)
