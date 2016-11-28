 Search Insert Position
 ====================
 Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

这道题让我们找插入的地方，难度其实不高，但是不知道为什么是M。

解法一： 线性遍历，O(n)

```
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] >= target) {
                return i;
            }
        }

        return nums.size();
    }
};
```

解法二：二分法

```
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0,right = nums.size(),mid = 0;

        while (left < right) {
            mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] > target) right = mid;
            else left = mid + 1;
        }

        return right;
    }
};
```

解法三：非常淫荡，将数插入数组，然后排序，再找到位置。时间复杂度取决于排序方法。

```
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        nums.push_back(target);
        sort(nums.begin(), nums.end());
        int res = 0;

        for (; res < nums.size(); res++) {
            if (nums[res] == target) return res;
        }

        return res;
    }
};
```
