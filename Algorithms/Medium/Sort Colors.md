Sort Colors
===========
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

这道题让我们排序颜色，实际上就是对一个乱序包含`0,1,2`的数组进行从小到大的排序。

解法：实际上解法挺多的，所有排序算法都可以解决，这里说一种非排序算法的。

我们可以使用两个变量`low`和`hight`，分别表示高位和低位，如果遇到2，全部都扔去高位，如果遇到0则去低位，这样就解决了。

```
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int hight = nums.size() - 1, low = 0;

        for (int i = 0; i < nums.size();) {
            if (nums[i] == 2) swap(nums[i], nums[hight--]);
            else if (nums[i] == 0) swap(nums[i++], nums[low++]);
            else i++;
            if (i > hight) break;
        }
    }
};
```
