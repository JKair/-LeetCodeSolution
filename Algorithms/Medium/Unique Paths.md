Unique Paths
=============
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

这道题让我们算出，在一个m * n的矩阵里面，左上角走到右下角有多少种走法。

解法一：这道题读起来，我第一反应是想到爬楼梯的问题，就是走一步走两步，问走到终点多少种走法，我们可以利用dp来做。

```
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int> (n, 1));
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }

        return dp[m-1][n-1];
    }
};
```

这里还可以优化内存，一行一行跑实际上也是可以的。

```
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j-1];
            }
        }

        return dp[n-1];
    }
};
```

解法二：[这里](http://blog.csdn.net/linhuanmars/article/details/22126357)实际上有一种数学思维的解法，把这个问题变为一个排列组合的问题，。机器人总共走的是m+n-2的步数，其中m-1步是往下走，n-1步是往右走，本质上是一个组合问题，就是从m+n-2个不同元素取出m-1个。然后我们根据排列组合的公司来解就好了。

```
class Solution {
public:
    int uniquePaths(int m, int n) {
        double dom = 1;
        double dedom = 1;
        int small = m<n? m-1:n-1;
        int big = m<n? n-1:m-1;
        for(int i=1;i<=small;i++)  
        {  
            dedom *= i;  
            dom *= small+big+1-i;  
        }  
        return (int)(dom/dedom);  
    }
};
```


相似题目[Unique Paths II](./Unique Paths II.md)
