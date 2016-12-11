Interleaving String
=============
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

这道题让我们判断s1+s2两个字符串按照顺序（就是不打乱字母重新编排）编排后是否能够变成s3。

解法：这道题是一个二维dp问题，难点在于推出递推式。

1. 首先，如果s1+s2的长度不等于s3，那么肯定返回false
1. 如果三者都为空，肯定返回true
1. 我们要创建一个`dp[n+1][m+1]`大小的数组，`dp[i][j]`代表的是，字符串s1的前i个字母+s2的前j个字母是否可以组成s3的前i+j个字母。
1. 首先我们要完成两条边的判断，就是当只有s1或者s2的时候，匹配的情况是如何的。
1. 接下来我们需要处理的是两个字符串互相串在一起的情况，`dp[i][j]`有两种情况要判断，第一种是处理当前匹配`s1[i - 1] == s[i + j - 1]`，就是加入s1字符串字母的时候，那么我们的`dp[i - 1][j]`也必须为true，意思就是加入第i个字母，那么前 i - 1 + j 个字母也应该匹配上，另一种情况则是加入s2字符串字母，则相反。由此我们可以得到递推式`dp[i][j] = (s3[i + j - 1] == s1[i - 1] && dp[i - 1][j]) || (s3[i + j - 1] == s2[j - 1] && dp[i][j - 1])`

具体分析过程如图：
```
  Ø d b b c a
Ø T F F F F F
a T F F F F F
a T T T T T F
b F T T F T F
c F F T T T T
c F F F T F T
```

代码如下：
```
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size(), m = s2.size(), r = s3.size();
        if (n + m != r) return false;
        else if (n == 0 && m == 0 && r == 0) return true;

        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        dp[0][0] = true;

        for (int i = 1; i <= n; i++) {
            dp[i][0] = ((s3[i - 1] == s1[i - 1]) && (dp[i - 1][0]));
        }

        for (int i = 1; i <= m; i++) {
            dp[0][i] = ((s3[i - 1] == s2[i - 1]) && (dp[0][i - 1]));
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                dp[i][j] = (s3[i + j - 1] == s1[i - 1] && dp[i - 1][j]) || (s3[i + j - 1] == s2[j - 1] && dp[i][j - 1]);
            }
        }

        return dp[n][m];
    }
};
```
