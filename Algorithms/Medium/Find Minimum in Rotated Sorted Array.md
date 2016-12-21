Find Minimum in Rotated Sorted Array
========
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

找到旋转排序过的数组的最小值。

解法：由于这道题的一开始是已经有序的，所以有个关键思路，就是二分法了，只要左边的数字小于中间的数字，那么我们就找右边的区域，否则则相反，跳出的条件是left和right，返回两个之中的最小值就可以了。

```
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        if (nums[left] > nums[right]) {
            while (left != right - 1) {
                int mid = (left + right) / 2;
                if (nums[mid] > nums[left]) left = mid;
                else right = mid;
            }
            return min(nums[left], nums[right]);
        }

        return nums[0];
    }
};
```
