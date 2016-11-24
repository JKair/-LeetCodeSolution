Longest Palindromic Substring
=============================

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

这道题让我们判断最长的回文串，直接暴力搜索是肯定玩不动的，超时杠杠的。

第一种解法：动态规划，用一个数组去记录每次判断的结果，`dp[j][i]`表示的是，从j到i的字符串是否回文。这里有三种情况，一种是`i=j`，那么则是自己，肯定是回文啦，第二种是`i-j=1`的情况，这种情况只有两个字符，只要`s[i]=s[j]`就可以了，然后大于2的情况，则是需要`(s[i] = s[j]) && dp[j+1][i-1]=1`。时间复杂度是O(n²)

```
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size(), dp[n][n] = {0},maxLen = 1,start=0;

        for (int i = 0; i < s.size(); i++) {
            for (int j = 0; j < i; j++) {
                dp[j][i] = (s[i] == s[j]) && ( i - j < 2 || dp[j + 1][i - 1]);

                if (dp[j][i] && maxLen < i - j + 1) {
                    start = j;
                    maxLen = i - j + 1;
                }
            }
            dp[i][i] = 1;
        }

        return s.substr(start, maxLen);
    }
};
```

第二种解法，叫做[马拉车算法](http://www.cnblogs.com/grandyang/p/4475985.html)，时间复杂度低达O(n)。

```
class Solution {
public:
    string longestPalindrome(string s) {
        string t ="$#";
        for (int i = 0; i < s.size(); ++i) {
            t += s[i];
            t += '#';
        }
        int p[t.size()] = {0}, id = 0, mx = 0, resId = 0, resMx = 0;
        for (int i = 0; i < t.size(); ++i) {
            p[i] = mx > i ? min(p[2 * id - i], mx - i) : 1;
            while (t[i + p[i]] == t[i - p[i]]) ++p[i];
            if (mx < i + p[i]) {
                mx = i + p[i];
                id = i;
            }
            if (resMx < p[i]) {
                resMx = p[i];
                resId = i;
            }
        }
        return s.substr((resId - resMx) / 2, resMx - 1);
    }
};
```
