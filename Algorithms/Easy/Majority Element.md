Majority Element
=========
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

这个让我们找一个众数，且出现的次数大于数组长度的一半。

解法：这里用摩尔投票法就可以解决问题了。

1. 我们可以知道，一个数组里面，出现的次数超过数组一半的数有且只有一个。
1. 我们从头到尾遍历一次，用一个变量记录出现次数，如果本次出现的数和正在投票的数一样，那么就计数器+1，否则-1
1. 当计数器等于0的时候，把数换成当前这个数
1. 最后得到的数就是我们要求的数了

```
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int res = 0, count = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (count == 0) {
                res = nums[i];
                count++;
            } else {
                nums[i] == res ? count++ : count--;
            }
        }

        return res;
    }
};
```

相似题目[Majority Element II](../Medium/Majority Element II.md)
