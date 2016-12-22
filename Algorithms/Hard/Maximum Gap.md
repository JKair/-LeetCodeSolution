Maximum Gap
========
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

给一个无序的数组，让我们计算它排序之后的状态，相邻的数间距最大的情况。

解法一：O(nlogn)的时间复杂度可以解决的，就是直接排序然后前后相减得出。

```
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int res = 0;
        for (int i = 1; i < nums.size(); i++) {
            res = max(nums[i] - nums[i - 1], res);
        }

        return res;
    }
};
```

解法二：题目实际上要求我们尽量用O(n)的时间复杂度去解决的，所以这里，我们能够解决的方案就有桶排序了，实际上桶排序本身是不难的一种排序方法，然而我们这里要用的是桶排序的一种发散性做法。

我们假设桶只有左右两个挡板，一个最大值一个最小值，代表了第n个序号桶的情况，我们只要将对应的大小值放进指定的桶，再桶的最小值去减掉前一个桶的最大值就是目前最大区间的候选值了。

那么问题在于，我们怎么知道应该将数放进哪个桶呢？根据[抽屉原理](http://baike.baidu.com/link?url=mfHjU-XtqjHZiLaAqYy87q_Re0v1KWh8GX3mfjCCKCN9L6wQJDE5MqnlevjKumxtYkfjN9nKo7eLk95XE8anUpMdSWn9dpoPbBJvlvsXQyIxyfwI9CQkViHcFp9N9dvz)。我们只要将最大值减去最小值，再除以整个数组的长度 + 1个`(maxNum - minNum) / nums.size() + 1`，就是总共我们需要的桶的个数，而且，最大值和最小值的差值永远不可能超过range-1。

我们用当前的值减最小值再除以桶的个数，就可以知道这个值应该放在哪里了，然后我们维护每个桶的最大值和最小值，完毕之后，在遍历每个桶，得知最大值和最小值。时间复杂度为O(n)!

```
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.size() < 2) return 0;
        int maxNum = nums[0], minNum = nums[0];

        for (int i = 0; i < nums.size(); i++) {
            maxNum = max(nums[i], maxNum);
            minNum = min(nums[i], minNum);
        }

        int range = (maxNum - minNum) / nums.size() + 1;

        map<int, vector<int>> buckets;
        for (int i = 0; i < nums.size(); i++) {
            int temp = (nums[i] - minNum) / range;

            if (buckets.find(temp) == buckets.end()) {
                buckets[temp] = {nums[i], nums[i]};
            } else {
                if (buckets[temp][0] > nums[i]) buckets[temp][0] = nums[i];
                if (buckets[temp][1] < nums[i]) buckets[temp][1] = nums[i];
            }
        }

        int res = 0;
        auto pre = buckets.begin();
        for (auto it = buckets.begin(); it != buckets.end(); it++) {
            res = max(it->second[0] - pre->second[1], res);
            pre = it;
        }

        return res;
    }
};
```
