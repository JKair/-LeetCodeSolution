Unique Binary Search Trees
=========================
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

这道题让我们列出n个数的搜索树有多少种可能的排列。

解法：实际上我也不知道这道题的解法，想列出所有的可能，但是A不了，最后超时，于是搜索了别人的解法。[这里](http://www.cnblogs.com/grandyang/p/4299608.html)，有详细的解释，可以推导出这道题实际上是一个卡塔兰数的问题。

```
class Solution {
public:
    int numTrees(int n) {
        vector<int> res(n+1, 0);
        res[0] = 1;
        res[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < i;j++) {
                res[i] += res[j] * res[i - j - 1];
            }
        }

        return res[n];
    }
};
```
