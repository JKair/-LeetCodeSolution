Find Minimum in Rotated Sorted Array II
==========
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

这里要我们做和`Find Minimum in Rotated Sorted Array`一样的工作，不同的是，这道题有相同值出现。

解法：思路和之前差不多，但是我们要多做一个操作，就是遇到相同值就跳过。

```
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size()-1;

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[right] < nums[mid]) left = mid + 1;
            else if (nums[mid] < nums[right]) right = mid;
            else {
                if (nums[left] == nums[mid]) {
                    left++;right--;
                } else right = mid;
            }
        }

        return nums[right];
    }
};
```

相似题目[Find Minimum in Rotated Sorted Array](../Medium/Find Minimum in Rotated Sorted Array.md)
