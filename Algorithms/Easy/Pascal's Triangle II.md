Pascal's Triangle II
==================
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

这道题是杨辉三角的扩展，但是这一次不是让我们生成一整个出来，而是只让我们生成某一行并且只能用O(n)的空间。

解法：由于我们只有n的空间，所以我们像之前，生成完之后再返回第n个是行不通的。可其实有一种很巧妙的方法，杨辉三角是对称的，所以其实我们从后往前扫描是完全没问题的，当是最后一个的时候，我们就push_back(1)，然后更新每个格子的值，等于还没更新的当前的格子加上-1个，即`res[j] = res[j] + res[j-1]`。

```
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0) return {1};
        vector<int> res(1, 1);

        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i; j > 0; j--) {
                if (j == i) res.push_back(1);
                else res[j] = res[j] + res[j - 1];
            }
        }

        return res;
    }
};
```
