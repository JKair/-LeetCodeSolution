Single Number
===========
Given an array of integers, every element appears twice except for one. Find that single one.

这道题给我们一个数组，然后只有一个数出现了一次，让我们找出那个数。

解法：最简便的解法就是利用位运算了，`^`异或运算，当相同的数字进行异或的时候，结果等于0，当任何数和0异或的时候等于那个数本身。

```
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (auto i:nums) {
            res ^= i;
        }
        return res;
    }
};
```

相似题目[Single Number II](../Medium/Single Number II.md)
