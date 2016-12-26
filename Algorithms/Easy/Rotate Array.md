Rotate Array
===========
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?

这道题让我们做数组旋转，并且额外的要求就是让我们只能用O(1)的空间。

解法一：我一开始的思路就是想通过交换数字来达到目的，交换的顺序如下

```
[1,2,3,4]
2
```

```
1 2 3 4
3 2 1 4
3 1 2 4
3 4 2 1
3 4 1 2
```

根据上面的思路，可以整理成代码
```
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        if (k == 0) return;

        int fast = n - k, slow = 0;
        while (fast < n) {
            int temp = slow;
            while (temp < fast)
                swap(nums[fast], nums[temp++]);
            slow++,fast++;
        }
    }
};
```
但是遗憾的是，最后一组大数过不了= =，超时了。

然后我看到一种解法，思路是我的改进版，减少了很多的交换次数，他的交换思想是这样的。
```
1 2 3 4
3 2 1 4
3 4 1 2
```
整理出来代码如下，自己纸画一下，这种思路确实比较巧妙，因为我们把后面k个数字交换到正确的位置了，那么也就是说交换到后面的k个数字的顺序也正确了，只是位置不正确，那么我们只要把钱k个到后k个中间的这些数，全部调到后面就可以了。
```
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.empty()) return;
        int n = nums.size(), start = 0;   
        while (n && (k %= n)) {
            for (int i = 0; i < k; ++i) {
                swap(nums[i + start], nums[n - k + i + start]);
            }
            n -= k;
            start += k;
        }
    }
};
```

解法二：我们可以先翻转后k个数字，再翻转前n-k个数字，再翻转整个数组，就可以了。

```
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (((k %= n) == 0) || nums.size() == 0) return;

        reverse(nums.begin() + n - k, nums.end());
        reverse(nums.begin(), nums.begin() + n - k);
        reverse(nums.begin(), nums.end());
    }
};
```

解法三：我们可以把后面的数字往前遍历k个，然后每个数字插入前面，删除后面，注意啊，这种做法是必须插入一个就删除一个，不然就不符合O(1)空间的要求了。

```
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (((k %= n) == 0) || nums.size() == 0) return;

        for (int i = n - 1; i >= n - k; i--) {
            nums.insert(nums.begin(), nums.back());
            nums.pop_back();
        }
    }
};
```
