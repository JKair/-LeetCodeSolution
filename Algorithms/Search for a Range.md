Search for a Range
=================
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

这道题让我们找出目标数的左边界和右边界。

解法一：我们可以先用二分法找出目标值的位置，然后由当前的位置往两边搜索寻找左边界和右边界。

```
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0,right = nums.size()-1;
        int mid;
        bool find = false;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (target > nums[mid]) left = mid+1;
            else if (target < nums[mid]) right = mid-1;
            else {
                find = true;
                left = mid;
                right = mid;
                break;
            }
        }
        vector<int> res(2, -1);
        if (!find) return res;

        while (nums[left] == target && left >= 0) left--;

        while (nums[right] == target && right < nums.size()) right++;

        res[0] = (++left);
        res[1] = (--right);

        return res;
    }
};
```
解法二：
