Merge Sorted Array
=================
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

这道题让我们将两个数组合并到第一个数组里面

解法一：使用插入法，好像插入排序一样，我们把这个当做插入排序进行到一半就可以了。由于nums1的已经预留了足够的空间，所以我们插入一个数就去掉最后面那个。另外，由于nums2数组已经是有序的了，我们可以通过记录上次插入的地方，

```
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (n == 0) return ;
        else if (m == 0) {
            nums1 = nums2;
            return;
        }

        int startIndex = 0;
        for (int i = 0; i < n; i++) {
            for (int j = startIndex; j <= m + i; j++) {
                if (j == m + i || nums1[j] >= nums2[i]) {
                    nums1.insert(nums1.begin()+j, nums2[i]);
                    nums1.pop_back();
                    startIndex = j;
                    break;
                }
            }
        }
    }
};
```
