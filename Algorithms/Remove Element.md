Remove Element
===============

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

这道题让我们删除和`val`一样的值

解法：我们用一个变量`res`去记录不等于`val`的个数，然后另外遍历数组去找寻不等于的数，如果找到了不等于，就直接往`res`的位置赋值就可以了。

```
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int res = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[res] = nums[i];
                res++;
            }
        }

        return res;
    }
};
```
