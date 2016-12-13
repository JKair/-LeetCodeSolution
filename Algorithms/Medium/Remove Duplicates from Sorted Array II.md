Remove Duplicates from Sorted Array II
====================
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

这个让我们去除排序数组中重复次数大于两次的数。

解法：应用快慢指针的思想就可以了。一个跑在前面，一个跑后面，如果先跑得指针等于慢的而且次数超过2次，那么就让前面的指针继续让前走，后面不动，否则则将数给赋值过来。

```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size();

        int res = 0, count = 0, i = 1;

        while (i < nums.size()) {
            if (nums[res] == nums[i] && count == 1) i++;
            else {
                if (nums[res] == nums[i]) count++;
                else count = 0;
                nums[++res] = nums[i++];
            }
        }

        return res + 1;
    }
};
```

相似题目[Remove Duplicates from Sorted Array](./Remove Duplicates from Sorted Array.md)
